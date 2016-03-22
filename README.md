# cpp2python

The script helps to convert C/C++ sources to C/C++ -like Python sources.

It does some simple edit operations like removing semicolons and type declarations.
After it you must edit code manually, but you'll probably spend less time doing it.

Example:
```
if (a && b)               -->    if a and b:
{                         -->        object.method()
    object->method();     -->
}                         -->
```

The utility **will** make mistakes and **will not** generate ready for use code,
therefore it won't be useful for you unless you know both C/C++ and Python.

For better result, it is recommended to format your code to ANSI style
before performing conversion.

```
astyle --style=ansi your.cpp source.cpp files.cpp
```

### Usage

    cpp2python.py DIR                     Find C/C++ files in the directory
                                          by suffix and process.
    cpp2python.py FILE                    Process the file
    cpp2python.py -v|--version|-h|--help  Display the help message

After the processing new file is created.
File name is `{old file name with suffix}.py`. i.e. `main.cpp.py`

### Installation
(Optional, the script can be used from the source tree)

    python3 setup.py install


### Author
Andrei Kopats <hlamer@tut.by>

setup.py and improvements by Stuart Axon

### License
GPL
