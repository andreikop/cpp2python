from setuptools import setup
import cpp2python

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

    scripts=['cpp2python.py']
)
