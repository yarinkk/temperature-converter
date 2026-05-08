"""
Module for temperature conversion.

Example:
>>> celsius_to_fahrenheit(0)
32.0

>>> celsius_to_fahrenheit(100)
212.0
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        ValueError: If input is not a number.
    """

    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number")

    return (celsius * 9 / 5) + 32