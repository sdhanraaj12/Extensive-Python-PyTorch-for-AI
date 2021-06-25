import pytest
import random
import session7
import os
import inspect
import re
import math
from random import randint
from session7 import *

# ------------------------ General Test Cases -----------------------------------

README_CONTENT_CHECK_FOR = ['Fibonacci', 'docstring', 'count', 'closure']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Make the format look good"


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"




def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__, "You have not documented the code!"

def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__, "You have not annotated the code!"

# ------------------------------------ Doc String Check function Test Case --------------------------

# Dummy function to test
def test_func_true():
    """
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    Function to check 50 characters doc string
    """
    return
# Dummy function to test
def test_func_false():
    """
    Less Doc
    """
    return

def test_check_dock_true():
    dc = check_doc_outer_fn()
    assert dc(test_func_true) == True, "Something wrong with the check_doc_fn function."


def test_check_dock_false():
    dc = check_doc_outer_fn()
    assert dc(test_func_false) == False, "Something wrong with the check_doc_fn function."


# ------------------------------------ Fibonacci Test Case --------------------------

def test_fibonacci():
    fib = fibonacci()
    assert fib() == 0, "Something wrong with the fibonacci function."
    assert fib() == 1, "Something wrong with the fibonacci function."
    assert fib() == 1, "Something wrong with the fibonacci function."
    assert fib() == 2, "Something wrong with the fibonacci function."
   
# ------------------------------------ Counter Test Case  --------------------------
def test_func_count():

    def add(a, b):
        return a+b
    def mul(a, b):
        return a*b
    def randomf():
        pass
    fc = func_counter()
    for i in range(5):
        fc(add, 2, 5)
    for i in range(3):
        fc(mul, 2, 5)
    for i in range(10):
        fc(randomf)
   
    
    assert session7.call_count['add'] == 5, "Something wrong with the func_count function."
    assert session7.call_count['mul'] == 3, "Something wrong with the func_count function."
    assert session7.call_count['randomf'] == 10, "Something wrong with the func_count function."

def test_func_count_check_error():
    with pytest.raises(TypeError):
        fc = func_counter()
        fc("Random Checks")

# ------------------------------------ Different Dictonary Test Case --------------------------

def test_func_count_with_dict_outer():

    def add(a, b):
        return a+b
    def mul(a, b):
        return a*b
    def randomf():
        pass

    dict_1 = dict()
    fc = func_count_with_dict_outer(dict_1)

    a, b, c = randint(1, 10),randint(1, 10),randint(1, 10)

    for i in range(a):
        fc(add, 2, 5)
    for i in range(b):
        fc(mul, 2, 5)
    for i in range(c):
        fc(randomf)

    assert dict_1['add'] == a, "Something wrong with the func_count function."
    assert dict_1['mul'] == b, "Something wrong with the func_count function."
    assert dict_1['randomf'] == c, "Something wrong with the func_count function."
  
    dict_2 = dict()
    fc_new = func_count_with_dict_outer(dict_2)

    a, b, c = randint(1, 10),randint(1, 10),randint(1, 10)

    for i in range(a):
        fc_new(add, 2, 5)
    for i in range(b):
        fc_new(mul, 2, 5)
    for i in range(c):
        fc_new(randomf)
    

    assert dict_2['add'] == a, "Something wrong with the func_count function."
    assert dict_2['mul'] == b, "Something wrong with the func_count function."
    assert dict_2['randomf'] == c, "Something wrong with the func_count function."


def test_func_count_with_dict_outer_check_error():
    with pytest.raises(TypeError):
        fc = func_count_with_dict_outer()
    
  
