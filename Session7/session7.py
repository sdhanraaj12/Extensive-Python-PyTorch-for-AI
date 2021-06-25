times_dict3={'add': 0, 'mul': 0, 'div': 0} 

def add(a:"Number1", b:"Number1")->"Sum of Numbers":
    """This Function Returns sum of Two given real numbers (Integer/Floats)"""
    return a + b


def mul(a:"Number1", b:"Number1")->"Multiplication of Numbers":
    """This Function Returns Multiplication of Two given real numbers(Integer/Floats)"""
    return a * b


def div(a:"Number1", b:"Number1")->"Division of Numbers":
    """This Function Returns division of Two given real numbers (Integer/Floats)"""
    return a / b if b != 0 else a


def function_1_docstring_50_count(fn):
    """
    This Closure function thats takes in function check if its docstring is having 50 character
    if yes then stores it in  free variable doc_string else it stores False Doc String not Long enough
    """
    doc_string = []
    def inner():
        nonlocal doc_string
        doc_string = str(fn.__doc__) if fn.__doc__ != None and len(
            fn.__doc__) >= 50 else "False Doc String not Long enough"
        return doc_string
    return inner


def function_2_fibonacci():
    """This Closure function gives the next fibonnaci number"""
    fibonnaci_series = [0]
    def inner():
        nonlocal fibonnaci_series
        if len(fibonnaci_series) == 1:
            fibonnaci_series.append(1)            
            return fibonnaci_series[-1]
        else:
            fibonnaci_series.append((fibonnaci_series[-1] + fibonnaci_series[-2]))            
            return fibonnaci_series[-1]
    return inner  


def function_3_counter(fn: "Function Name for Counter"):
    """This Function creates a counter for input function and updates the global dictionary times_dict3"""                   
    def inner(*args, **kwargs):        
        times_dict3[fn.__name__] += 1
        return fn(*args, **kwargs),times_dict3
    return inner


def function_4_counter(fn: "Function Name for Counter", dict: "Input dictory name"):
    """This Function creates a counter for input function and updates it in given dictionary"""    
    def inner(*args, **kwargs):
        dict[fn.__name__] += 1
        return fn(*args, **kwargs)
    return inner