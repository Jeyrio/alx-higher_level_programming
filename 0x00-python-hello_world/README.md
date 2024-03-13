# README FILE

## 0x00. Python - Hello, World

### Resources
Read or watch:

[The Python tutorial](https://docs.python.org/3/tutorial/index.html)
[Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
[An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
[How To Use String Formatters in Python 3](https://realpython.com/python-f-strings//)
[Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
[Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)


### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
1. Why Python programming is awesome
2. Who created Python
3. Who is Guido van Rossum
4. Where does the name ‘Python’ come from
5. What is the Zen of Python
6. How to use the Python interpreter
7. How to print text and variables using print
8. How to use strings
9. What are indexing and slicing in Python
10. What is the official Python coding style and how to check your code with pycodestyle

### Copyright - Plagiarism
1. You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
2. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
3. You are not allowed to publish any content of this project.
4. Any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements
#### Python Scripts

1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file at the root of the repo, containing a description of the repository
6. A README.md file, at the root of the folder of this project, is mandatory
7. Your code should use the pycodestyle (version 2.8.*)
8. All your files must be executable
9. The length of your files will be tested using wc

#### Shell Scripts

1. Allowed editors: vi, vim, emacs
2. All your scripts will be tested on Ubuntu 20.04 LTS
3. All your scripts should be exactly two lines long (wc -l file should print 2)
4. All your files should end with a new line
The first line of all your files should be exactly #!/bin/bash
5. All your files must be executable

#### C Scripts
1. Allowed editors: vi, vim, emacs
2. All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
3. All your files should end with a new line
4. Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
5. You are not allowed to use global variables
6. No more than 5 functions per file
7. In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
8. The prototypes of all your functions should be included in your header file called lists.h
9. Don’t forget to push your header file
10. All your header files should be include guarded

### More Info
#### Zen

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

##TASKS

0. \* Run Python file [0-run](./0-run) - Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE

1. Run inline [1-run_inline](./1-run_inline) - Write a Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE

2. Hello, print [2-print.py](./2-print.py) - Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
Use the function print

3. Print integer [3-print_number.py](./3-print_number.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line also using [f-strings](https://realpython.com/python-f-strings/).

4. Print float [4-print_float.py](./4-print_float.py) - Complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits using f-strings.

5. Print string [5-print_string.py](./5-print_string.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters

6. Play with strings [6-concat.py](./6-concat.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School! 

7. Copy - Cut - Paste [7-edges.py](./7-edges,py0) - Copy - Cut - Paste, Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

8. Create a new sentence [8-concat_edges.py](./8-concat_edges.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

9. Easter Egg [9-easter_egg.py](./9-easter_egg.py) - Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

10. Linked list cycle [10-check_cycle.c, lists.h](./10-check_cycle) - Write a function in C that checks if a singly linked list has a cycle in it.
Prototype: int check_cycle(listint_t *list);
/*Return: 0 if there is no cycle, 1 if there is a cycle

11. Hello, write [100-write.py](./100-write.py) - Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
12. Compile [101-compile](./101-compile) - Write a script that compiles a Python script file.
The Python file name will be stored in the environment variable $PYFILE
The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
13. ByteCode -> Python #1 [102-magic_calculation.py](./102-magic_calculation.py) - Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode */
