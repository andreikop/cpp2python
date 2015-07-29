import os
import subprocess
import sys
import pkg_resources

import subprocess
import sys

from glob import glob
from os.path import abspath, basename, dirname, join, normpath, relpath
from shutil import rmtree
from textwrap import dedent

from setuptools import setup
from setuptools import Command
import cpp2python

here = normpath(abspath(dirname(__file__)))

setup(
    name='cpp2python',
    version='0.2.0',
    description='Helps to convert C/C++ sources to C/C++ -like Python sources.',
    long_description=cpp2python.help,
    url='https://github.com/hlamer/cpp2python',
    author='Andrei Kopats',
    author_email='hlamer@tut.by',
    license='GPL',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='cpp python',

    entry_points = {
            'console_scripts': [
                'cpp2python = cpp2python:main'
            ]
        },
)
