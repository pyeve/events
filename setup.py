#!/usr/bin/env python

from setuptools import setup, find_packages

DESCRIPTION = ("Bringing the elegance of C# EventHandler to Python")
VERSION = __import__('events').__version__
with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='Events',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Nicola Iarocci',
    author_email='nicola@nicolaiarocci.com',
    url='http://github.com/pyeve/events',
    license="BSD",
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ],
)
