from typing import List


def capitalize_words(words: List[str]) -> List[str]:
    """Return a new list with each word capitalized."""
    return [word.capitalize() for word in words]


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Return only even numbers from a list."""
    return [n for n in numbers if n % 2 == 0]


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b. Raises ValueError for zero divisor."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
