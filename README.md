# cpp2python
Script helps to convert C/C++ sources to C/C++ -like Python sources.

It does few simple edit operations, like removing semicolons and type declarations. After it you must edit code manually, but you'll spend less time to do it.

Utility **will** make mistaces and **will not** generate ready for use code, so, it won't help you, unless if you know either C/C++ and Python

For better result, it is recomented to format your code to ANSI style before doing conversion.

**NO ANY BACKUPS ARE CREATED. YOU MAY PERMANENTLY CORRUPT YOR SOURCES**

Usage:
    
    cpp2python.py DIR|FILE
    cpp2python.py -v|--version|-h|--help

When directory name is given - tries to find source files by C/C++ suffixes, when file name is given - processes given file

Author: Andrei Kopats <hlamer@tut.by>
License: GPL
