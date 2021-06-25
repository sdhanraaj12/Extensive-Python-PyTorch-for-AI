# Assignment for Session 7
### Created by Shashwat Dhanraaj
## Assignment states:

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200
- Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250
- Once done, upload the code to github, run actions, and then proceed to answer S7 - Assignment Solutions. 
- No readme or no docstring for each function, or no test cases (4, 2, 6, 6 tests), then 0 . Write test cases to check boundary conditions that might cause your code to fail. You mustg write the tests that are MOST important and what "I" already have in my mind 🤯↷🧠

## Functions used in main assignment file ([ session7.py](https://github.com/sdhanraaj12/Extensive_Python_PyTorch_for_AI/blob/master/Session7/session7.py))
### function_1_docstring_50_count(fn):
    """
    This Closure function thats takes in function check if its docstring is having 50 character
    if yes then stores it in  free variable doc_string else it stores False Doc String not Long enough
    """

### function_2_fibonacci():
    """
    This Closure function gives the next fibonnaci number
    """

### function_3_counter (fn: "Function Name for Counter"):
    """
    This Function creates a counter for input function and updates the global dictionary times_dict3
    """
### function_4_counter (fn: "Function Name for Counter", dict: "Input dictory name"):
    """
    This Function creates a counter for input function and updates it in given dictionary
    """
### add (a:"Number1", b"Number1")->"Sum of Numbers":
    """
    This Function Returns sum of Two given real numbers (Integer/Floats)
    """
### mul (a:"Number1", b"Number1")->"Multiplication of Numbers":
    """
    This Function Returns Multiplication of Two given real numbers (Integer/Floats)
    """
### div (a:"Number1", b"Number1")->"Division of Numbers":
    """
    This Function Returns division of Two given real numbers (Integer/Floats)
    """
