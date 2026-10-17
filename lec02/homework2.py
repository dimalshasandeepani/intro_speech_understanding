'''
This homework defines one method, called "arithmetic".
that method, type `help homework2.arithmetic`.
'''

def arithmetic(x, y):
    """
    Modify this code so it performs one of four possible functions
    """
    if isinstance(x, str) and isinstance(y, str):
        return x + y
    elif isinstance(x, str) and not isinstance(y, str):
        return x * int(y)
    elif not isinstance(x, str) and isinstance(y, str):
        return str(x) + y
    else:
        return x * y