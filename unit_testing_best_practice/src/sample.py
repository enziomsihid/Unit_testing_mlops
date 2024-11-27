## FUNCTION TO TEST ##

def func(x):
    return x + 1

def username_check(username) :
    #RETURNS 0 IF THE username IS
    #EMPTY OR CONTAINS AN EMPTY CHARACTER
    #RETURNS 1 OTHERWISE
    username = str(username)

    if len(username) == 0 :
        print("Is empty")
        return 0

    for i in range(len(username)) :
        if username[i] == " " :
            print("Contains a space")
            return 0
    return 1

def password_check(password) :
    contains_number = 0
    contains_letter = 0
    contains_special = 0
    password = str(password)
    if len(password) < 8 :
        print("Is too short")
        return 0

    for i in range(len(password)) :
        if password[i].isnumeric() == True :
            contains_number +=1

        if password[i].isalpha() == True :
            contains_letter +=1

        if not password[i].isalnum() :
            contains_special +=1

    if contains_number == 0 :
        print("Does not Contain Number")
        return 0

    if contains_letter == 0 :
        print("Does not Contain Letter")
        return 0

    if contains_special == 0 :
        print("Does not Contain Special Character")
        return 0

    return 1


def mail_check(mail: str) -> int :
    at = 0
    dot = 0
    mail = str(mail)
    for i in range(len(mail)) :
        if mail[i] == "@" :
            at += 1
        if mail[i] == ".":
            dot +=1

    if at == 0 or dot == 0 :
        print("Missing @ or .")
        return 0

    else :
        return 1

def find_sign(a: int, b: int) -> str:
    summation = a + b
    if summation > 0:
        ans = "positive"
    else:
        ans = "negative"
    return ans

#### OTHER WAY / CLEANER FOR TEST AND CUN ####
# The simplest function to get the user email (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Tell me your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

# Tests (copy to tests/test_user_functions.py)
#import pytest
#import io
#from user_functions import *

#def test_email_with_user_input_no_at_sign(monkeypatch):
#    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
#    assert get_email_from_input() is None

# def test_email_with_user_input_no_dot(monkeypatch):
#     monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
#     assert get_email_from_input() is None
#
# def test_email_with_user_input_correct(monkeypatch):
#     monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
#     assert get_email_from_input() == 'petra@adaltas.com'
#
# # Do the same for the following functions
# # Functions in src/user_functions.py and tests in tests/test_user_functions.py
#
# def get_user_name_from_input():
#     """ Not empty string. No spaces. """
#     return input("Create your user name: ")
#
# def get_password_from_input():
#     """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
#     return input("Create your password: ")
