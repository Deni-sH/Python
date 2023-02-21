
from fizzbuzz import fizzbuzz
import pytest


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

    
def test_fizzbuzz1():
    assert fizzbuzz(4) == "4"