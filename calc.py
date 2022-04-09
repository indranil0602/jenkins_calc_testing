def add(x, y):
    return x + y

def substruct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divison(x, y):
    if y == 0:
        raise ValueError('cannot divided by zero')
    return x / y

def modulo(x, y):
    return x % y