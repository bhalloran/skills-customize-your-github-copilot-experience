import pytest

from starter_code import capitalize_words, filter_even_numbers, divide


def test_capitalize_words():
    assert capitalize_words(["hello", "world"]) == ["Hello", "World"]
    assert capitalize_words([""]) == [""]


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even_numbers([]) == []


def test_divide():
    assert divide(10, 2) == 5
    assert divide(5.5, 2.2) == pytest.approx(2.5)


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
