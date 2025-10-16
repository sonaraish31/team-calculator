# advanced.py
"""Advanced mathematical operations."""
import math

def sqrt(x):
    """Return square root of x; raises ValueError if x < 0."""
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def power(base, exponent):
    """Return base ** exponent."""
    return pow(base, exponent)

def percentage(part, whole):
    """Return what percent 'part' is of 'whole' (0-100)."""
    if whole == 0:
        raise ValueError("Whole must not be zero to calculate percentage.")
    return (part / whole) * 100
