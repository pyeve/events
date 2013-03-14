#!/usr/bin/env python

from setuptools import setup, find_packages

DESCRIPTION = ("Bringing the elegance of C# EventHanlder to Python")
LONG_DESCRIPTION = open('README.rst').read()
VERSION = __import__('events').__version__

setup(
    name='Events',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Nicola Iarocci',
    author_email='nicola@nicolaiarocci.com',
    url='http://github.com/nicolaiarocci/events',
    license=open('LICENSE').read(),
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    test_suite="events.tests",
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
