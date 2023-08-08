# Python interpreter description
## taken from the book
## A Beginners Guide to Python 3 Programming
### Author: John Hunt
The way in which the Python interpreter processes a Python program is broken
down into several steps. The steps shown here are illustrative (and simplified) but
the general idea is correct:
1. First the program is checked to make sure that it is valid Python. That is a check
is made that the program follows all the rules of the language and that each of
the commands and operations etc. is understood by the Python environment.
2. It then translates the plain text, English like commands, into a more concise
intermediate format that is easier to execute on a computer. Python can store this
intermediate version in a file which is named after the original file but with a '.
pyc' extension instead of a '.py' extension (the 'c' in the extension indicates it
contains the compiled version of the code).
3. The compiled intermediate version is then executed by the interpreter.
When this program is rerun, the Python interpreter checks to see if a '.pyc' file
is present. If no changes have been made to the source file since the '.pyc' was
4. Introduction
created, then the interpreter can skip steps 1 and 2 and immediately run the '.pyc'
version of the program.
One interesting aspect of Python’s usage is that it can be (and often is) used in an
interactive fashion (via the REPL), with individual commands being entered and
executed one at a time, with context information being built up. This can be useful
in debugging situations.

## Scripting
It is also possible to transform a file containing a stored Python program into a
Script. A script is a stand-alone file that can be run directly without the need to
(explicitly) use the python command.
This is done by adding a special line to the start of the Python file that indicates
the Python command (or interpreter) to use with the rest of the file. This line must
start with '#!' and must come at the start of the file
e.g. #!/usr/local/bin/python3
> also make it exectuable with $ chmod +x hello.py
> i.e. the python file becomes an executable on unix systems, probably works similarly on windows aswell.
