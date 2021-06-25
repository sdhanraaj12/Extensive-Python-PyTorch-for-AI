from collections import Callable
def check_doc_outer_fn() -> 'Function':
    """
    Function to implement closure, encapsulates a function
    that checks whether an given function has docstring with more than 50 characters
    """
    min_character_len = 50

    def check_doc_inner_fn(fn: 'Function') -> 'Boolean':
        """
        This is the inner function that checks the 
        docstring legth.
        Input: Function for which the docs has to be checked.
        Output: True if doc string length > 50 else False

        """
        if not isinstance(fn, Callable):
            raise TypeError("Expected function!")

        return True if(len(fn.__doc__) >= min_character_len) else False

    return check_doc_inner_fn

# Write a closure that gives you the next Fibonacci number 
def fibonacci() -> "Function":

    """
    Function to implement closure, encapsulates a function
    that automatically gives you the fibonacci number.
    """
    num_1, num_2,count = 0, 1,0

    def next_fibbonacci_number() -> "Number":
        """
        Returns the next fibonacci number in the sequence.
        """
        nonlocal num_1, num_2, count

        if(count == 0):
            count+=1
            return 0
        elif(count==1):
            count+=1
            return num_2
        else:
            num_1, num_2 = num_2, num_1+num_2
            return num_2

    return next_fibbonacci_number

call_count = {}

def func_counter() -> "Function":
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a global list with count, and
    also mantains a free variable list so as to not let user 
    alter the count.

    """
    call_count_free = {}
    def func_counter_inside(func: "Function", *args, **kwargs) -> "":
        """
        Inner function that actually Updates and keeps track
        of the number of times,a function might be called.

        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        global call_count
        nonlocal call_count_free
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        func_name = func.__name__
        count = call_count_free.get(func_name, 0)
        call_count_free[func_name] = count + 1
        call_count = call_count_free

        return func(*args, **kwargs)

    return func_counter_inside

# Modify above such that now we can pass in different dictionary variables to update different dictionaries

def func_count_with_dict_outer(count_dict : dict) -> "Function":
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a dictionary given in the input

    """
    if type(count_dict) != dict:
        raise TypeError("Expected dictionary!")

    def func_count_with_dict_inner(func: "Function", *args, **kwargs) -> "Function called with provided parameters.":
        """
        Updates and keeps track of the number of times, 
        a function might be called.
        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        nonlocal count_dict 

        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        func_name = func.__name__
        count = count_dict.get(func_name, 0)
        count_dict[func_name] = count + 1

        return func(*args, **kwargs)

    return func_count_with_dict_inner
