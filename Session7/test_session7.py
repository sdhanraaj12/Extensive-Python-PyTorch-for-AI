import pytest
import random
from random import randint

import session7
from session7 import function_1_docstring_50_count
from session7 import function_2_fibonacci
from session7 import function_3_counter
from session7 import function_4_counter
from session7 import add
from session7 import div
from session7 import mul


import os
import inspect
import re
import random

README_CONTENT_CHECK_FOR = [
    'function_1_docstring_50_count',
    'function_2_fibonacci',
    'function_3_counter',
    'function_4_counter',
    'add',
    'mul',
    'div'
 ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

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
 
def test_function_1_docstring_50_count():
    check1=function_1_docstring_50_count(function_3_counter)
    check2=function_1_docstring_50_count(function_4_counter)    
    assert check1()=="This Function creates a counter for input function and updates the global dictionary times_dict3", "Check function_1_docstring_50_count not working properly"
    assert check2()=="This Function creates a counter for input function and updates it in given dictionary", "Check function_1_docstring_50_count not working properly"

def test_function_2_fibonacci():
    check1=function_2_fibonacci()
    for i in range(10):
        test=check1()    
    assert test== 55,"Check function_2_fibonacci "
 

def test_function_3_counter():
    counter_add=function_3_counter(add)
    counter_mul=function_3_counter(mul)
    counter_div=function_3_counter(div)    
    for i in range(5):
        test1,times_dict3=counter_add(randint(-100,100),randint(-100,100))        
    for j in range(3):
        test2,times_dict3=counter_mul(randint(-100,100),randint(-100,100))               
    for j in range(10):
       test3,times_dict3=counter_div(randint(-100,100),randint(-100,100))                 
    assert times_dict3=={'add': 5, 'mul': 3, 'div': 10},"Check function_3_counter "    
 
def test_function_4_counter():
    times_dict4={'add': 0, 'mul': 0, 'div': 0}
    counter_add=function_4_counter(add,times_dict4)
    counter_mul=function_4_counter(mul,times_dict4)
    counter_div=function_4_counter(div,times_dict4)
    for i in range(5):
        test1=counter_add(randint(-100,100),randint(-100,100))
    for j in range(3):
        test2=counter_mul(randint(-100,100),randint(-100,100))       
    for j in range(10):
       test3=counter_div(randint(-100,100),randint(-100,100))      
    assert times_dict4=={'add': 5, 'mul': 3, 'div': 10}, "Check function_4_counter "      