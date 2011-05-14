=========
daterange
=========

Installation
------------

::

  $ python setup.py install


Usage
-----

daterange is a simple Python module and command-line wrapper for generating
dates. For example, in Python:

::

  >>> from daterange import daterange
  >>> from datetime import date
  >>> print list(daterange(date(2011, 1, 1), days=10))
  [datetime.date(2011, 1, 1), datetime.date(2011, 1, 2), ...]

or from the command-line:

::

  $ dr -s 2011-01-01 -d 10
  2011-01-01
  2011-01-02
  ...

See ``dr --help`` for usage information.
