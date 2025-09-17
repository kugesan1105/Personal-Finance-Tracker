"""
Mathematical Operations Utilities

Provides basic mathematical helper functions for calculations
commonly used throughout the application.
"""

from typing import List, Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.
    
    Args:
        a (Union[int, float]): The first number
        b (Union[int, float]): The second number
    
    Returns:
        Union[int, float]: The sum of a and b
    """
    return a + b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers together.
    
    Args:
        a (Union[int, float]): The first number
        b (Union[int, float]): The second number
    
    Returns:
        Union[int, float]: The product of a and b
    """
    return a * b


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the average (mean) of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers
    
    Returns:
        float: The average of the numbers
    
    Raises:
        ValueError: If the list is empty
        TypeError: If any element in the list is not a number
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers")
    
    return sum(numbers) / len(numbers)


def percentage_change(old_value: Union[int, float], new_value: Union[int, float]) -> float:
    """
    Calculates the percentage change between two values.
    
    Args:
        old_value (Union[int, float]): The original value
        new_value (Union[int, float]): The new value
    
    Returns:
        float: The percentage change (positive for increase, negative for decrease)
    
    Raises:
        ZeroDivisionError: If the old_value is zero
    """
    if old_value == 0:
        raise ZeroDivisionError("Cannot calculate percentage change when old value is zero")
    
    return ((new_value - old_value) / old_value) * 100