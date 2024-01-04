#!/bin/bash

########################################################################
########################################################################

# https://tangenttechnologies.ca/blog/geany-python/

# You're going to want to make sure you have Python installed first off.  This is all you need to start coding in Python.
sudo apt-get install Python

# I also recommend installing the Python code checker and linter commands.  These commands will check your code style to ensure you are formatting your code properly.

# pycodestyle checks your code formatting
sudo apt install pycodestyle

# pyflakes checks your dependencies and import statements
sudo apt install pyflakes

sudo apt install pylint
pip install pylint --upgrade

# These commands can be used from a terminal to check your python files.  For example
pycodestyle main.py

# But you can also integrate them into Geany.

########################################################################
########################################################################

# Check the version of the 'python' symlink
ls -l $(which python)

# Check the version of the 'pip' symlink
ls -l $(which pip)

# If 'python' points to Python 2 and you want it to point to Python 3:
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# If 'pip' points to the Python 2 version and you want it to point to the Python 3 version:
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
