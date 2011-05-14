''' 
daterange: a generator function and CLI wrapper for generating lists of dates

>>> list(daterange(date(2011, 1, 1), days=10, step=7))
[datetime.date(2011, 1, 1), datetime.date(2011, 1, 8)]
>>> list(daterange(date(2011, 1, 1), end=date(2010, 12, 30)))
[datetime.date(2011, 1, 1), datetime.date(2010, 12, 31)]
'''

from datetime import date, timedelta
import sys
import time

def done_func(end, step, exclusive=True):
    '''
    Returns a function to determine whether a particular date has passed the
    end date.

    >>> start = date(2011, 1, 1)
    >>> end = date(2011, 2, 1)
    >>> end_before = date(2010, 12, 1)
    >>> done = done_func(end, 1)
    >>> done(start)
    False
    >>> done = done_func(end_before, 1)
    >>> done(start)
    True
    >>> done = done_func(end_before, -1)
    >>> done(start)
    False
    '''
    def done(day):
        '''
        Returns true if the given day has not reached the end date.
        '''
        if end and not exclusive:
            return (step > 0 and day > end) or (step < 0 and day < end)
        elif end and exclusive:
            return (step > 0 and day >= end) or (step < 0 and day <= end)
        return False
    return done

def daterange(start, step=1, end=None, days=None, exclusive=True):
    '''
    Generates a list of dates, starting from the start date, increasing by step
    days, until either the end date has been reached (inclusive; if there was
    one) or the number of generated days reaches "days".

    >>> start = date(2011, 1, 1)
    >>> dates = list(daterange(start, step=1, days=3))
    >>> dates[0].strftime('%Y-%m-%d')
    '2011-01-01'
    >>> dates[1].strftime('%Y-%m-%d')
    '2011-01-02'
    >>> dates[2].strftime('%Y-%m-%d')
    '2011-01-03'
    >>> len(dates)
    3
    >>> end = date(2010, 12, 28)
    >>> dates = list(daterange(start, step=-3, end=end))
    >>> dates[0].strftime('%Y-%m-%d')
    '2011-01-01'
    >>> dates[1].strftime('%Y-%m-%d')
    '2010-12-29'
    >>> len(dates)
    2
    '''
    if not start or step == 0:
        return
    if end and end < start and step > 0:
        step = -step
    astep = abs(step)
    count = 0
    day = start
    done = done_func(end, step, exclusive)
    while not done(day) and (not days or count < days):
        yield day
        day += timedelta(days=step)
        count += astep

def parse_date(option, opt_str, value, parser):
    '''
    An optparse callback for converting and storing a string argument as a
    date object.
    '''
    parsed_date = date(*(time.strptime(value, '%Y-%m-%d')[0:3]))
    setattr(parser.values, option.dest, parsed_date)

def print_dates(start, out=None, date_fmt='%Y-%m-%d', **opts):
    '''
    Prints dates using daterange() to an output stream (sys.stdout by default).
    Keyword args are passed through to daterange.
    '''
    if out is None:
        out = sys.stdout
    for next_date in daterange(start, **opts):
        print >> out, next_date.strftime(date_fmt)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
