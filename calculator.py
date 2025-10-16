# calculator.py
"""Basic arithmetic operations."""

def add(a, b):
    """Return a + b"""
    return a + b

def subtract(a, b):
    """Return a - b"""
    return a - b

def multiply(a, b):
    """Return a * b"""
    return a * b

def divide(a, b):
    """Return a / b; raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b