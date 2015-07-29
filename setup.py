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

here = normpath(abspath(dirname(__file__)))    

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info ./__pycache__'.split(' ')

    user_options = []

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        global here

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob(normpath(join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % relpath(path))
                try:
                    rmtree(path)
                except:
                    pass

long_description=dedent("""
    cpp2python

    Script helps to convert C/C++ sources to C/C++ -like Python sources.

    It does few simple edit operations, like removing semicolons and type declarations. After it you must edit code manually, but you'll spend less time to do it.

    Utility will make mistaces and will not generate ready for use code, so, it won't help you, unless if you know either C/C++ and Python

    For better result, it is recomented to format your code to ANSI style before doing conversion.

    NO ANY BACKUPS ARE CREATED. YOU MAY PERMANENTLY CORRUPT YOR SOURCES

    Usage:

    cpp2python.py DIR|FILE
    cpp2python.py -v|--version|-h|--help

    When directory name is given - tries to find source files by C/C++ suffixes, when file name is given - processes given file

    Author: Andrei Kopats hlamer@tut.by License: GPL
""")

setup(
    cmdclass={
        'clean': CleanCommand,
    },

    name='cpp2python',
    version='0.1.0',

    description='Helps to convert C/C++ sources to C/C++ -like Python sources.',
    long_description=long_description,
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
