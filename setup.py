from setuptools import setup, find_packages

'''
setuptools installation script for the daterange module
'''

setup(
    name = "daterange",
    version = "0.1",
    packages = find_packages(),
    scripts = ['dr'],
    author = "Matt Papi",
    author_email = "mmpapi@gmail.com",
    description = "Generates lists of dates",
    license = "MIT",
    url = "http://github.com/mpapi/daterange"
)
