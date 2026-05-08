import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.converter import celsius_to_fahrenheit


def test_zero_temperature():
    assert celsius_to_fahrenheit(0) == 32.0


def test_positive_temperature():
    assert celsius_to_fahrenheit(100) == 212.0


def test_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40.0


def test_float_temperature():
    assert round(celsius_to_fahrenheit(36.6), 2) == 97.88


def test_invalid_input():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit("abc")