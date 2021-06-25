# Session 7 -  Assignment
### by Shashwat Dhanraaj
## Assignment states:

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200
- Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250
- Once done, upload the code to github, run actions, and then proceed to answer S7 - Assignment Solutions. 
- No readme or no docstring for each function, or no test cases (4, 2, 6, 6 tests), then 0 . Write test cases to check boundary conditions that might cause your code to fail. You mustg write the tests that are MOST important and what "I" already have in my mind 🤯↷🧠

## Functions used in main assignment file ([ session7.py](https://github.com/sdhanraaj12/Extensive_Python_PyTorch_for_AI/blob/master/Session7/session7.py))

**Contents**
- check_docstring
- generate_fibanoci
- function_counter
- function_counter_mod

### check_docstring

    def check_docstring(max_len) -> 'Function': 
        def docstring_fifty(func) -> 'bool':            
            result = len(func.__doc__) > max_len
            return result
        return docstring_fifty

- Checks if a given function has docstring more than max_len variable
- max_len is a free variable which can be checked with __code__.co_freevars function. its a test in testfile

### generate_fibanoci

    def generate_fibanoci() -> 'Function': 
        n = 0    
        def next_Fib() -> 'Integer' :
            a = 0
            b = 1
            c = 0
            nonlocal n    
            if (n==0):
                n = n + 1            
                return 0
            elif n==1:
                n = n + 1            
                return b 
            else:            
                for i in range(1,n):
                    c = a + b
                    a = b
                    b = c 
                n = n + 1
                return b
        return next_Fib

- Fibnoci algorithm is fed at next_fib() closure function . n is a non local variable used as a counter to remember how many times a function(next_fib()) is called.


### function_counter

    def function_counter() -> 'Function':        
        count = dict()
        def inner(fn,*args, **kwargs) -> 'Function(*args, **kwargs)':           
            nonlocal count 
            count[fn.__name__] = count.get(fn.__name__, 0) + 1
            function_call_counter[fn.__name__] = count[fn.__name__] 
            return fn(*args, **kwargs)
        return inner

- A global dictionary 'function_call_counter' is used  , count is sued to remmeber number of times each function is called. 'count' is used as a nonlocal variable that can used to reset if 'function_call_counter' is modified by some other function.

### function_counter_mod

    def function_counter_mod(user_dict) -> 'Function':
        def inner(fn, *args, **kwargs) -> 'Function':
            user_dict[fn.__name__] = user_dict.get(fn.__name__, 0) + 1
            return fn(*args, **kwargs)
        return inner 

- A user defined dictionary 'user_dict' is given as input and used  , User provided dictionary
is directly modified inside the function every time when a particular function is called.


