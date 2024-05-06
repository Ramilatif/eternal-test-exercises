def add(x, y):
    """Addition function."""
    return x + y

def subtract(x, y):
    """Subtraction function."""
    return x - y

def multiply(x, y):
    """Multiplication function."""
    return x * y

def divide(x, y):
    """Division function."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

"""écrire les tests unitaires pour ces fonctions.
atteindre un coverage de 100%
"""

assert add(10,10)== 20
assert add(10,-10)== 0

assert subtract(10,10) ==0
assert subtract(10,-10) == 20

assert multiply(10,10) == 100
assert multiply(10,-10)== -100

assert divide (10,2) == 5
assert divide (10,0) == ValueError("Cannot divide by zero!")