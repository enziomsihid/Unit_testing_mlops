## TEST FUNCTION IN SAMPLE.PY in src folder in previous folder##


import pytest
import sys #Import locations of files in our Sys
import os 

#Modifying the main way we look at the path because its not always run from this folder...

# Get the absolute path of the 'src' directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
# Add the absolute path of the 'src' directory to sys.path
sys.path.append(src_dir)


from sample import *
#From sample.py file, we import all functions.

def test_answer():
    assert func(3) == 4


def test_username_check():
    assert username_check("u 12") == 0
    assert username_check("") == 0
    assert username_check("josiane") == 1

def test_password_check():
    assert password_check("Password1!") == 1
    assert password_check("short1!") == 0  # Less than 8 characters
    assert password_check("password!") == 0  # No number
    assert password_check("12345678!") == 0  # No letter
    assert password_check("Password1") == 0  # No special character


def test_mail_check():
    assert mail_check("user@example.com") == 1
    assert mail_check("userexample.com") == 0  # Missing '@'
    assert mail_check("user@com") == 0  # Missing '.'


#coverage run -m pytest
#coverage report -m


#Now we can go in the terminal in /test and run pytest.
