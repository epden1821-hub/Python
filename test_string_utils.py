import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# -------------------------------
# ТЕСТЫ ДЛЯ capitalize
# -------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# -------------------------------
# ТЕСТЫ ДЛЯ trim
# -------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("      Слева", "Слева"),
    ("      123", "123"),
    ("      14 апреля 2025", "14 апреля 2025"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_value", [
    None,
    123,
    ["text"],
])
def test_trim_negative_invalid_type(input_value):
    with pytest.raises(AttributeError):
        string_utils.trim(input_value)

# -------------------------------
# ТЕСТЫ ДЛЯ contains
# -------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "U", False),
    ("", "a", False),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
def test_contains_negative_empty_symbol():
    """
    symbol = "" — это не символ, но метод возвращает True.
    Это явный дефект.
    """
    assert string_utils.contains("hello", "") is True  # index("") всегда 0 → баг


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("hello", None),
    (123, "1"),
])
def test_contains_negative_wrong_type(string, symbol):
    with pytest.raises(Exception):
        string_utils.contains(string, symbol)


@pytest.mark.negative
def test_contains_negative_many_chars():
    """
    Метод называется contains(symbol),
    но если передать строку из нескольких символов,
    он считает это нормальным.
    """
    assert string_utils.contains("hello", "he") is True  # 'he' — не символ, но метод принимает → дефект


# -------------------------------
# ТЕСТЫ ДЛЯ delete_symbol
# -------------------------------

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaaa", "a", ""),       # удаляет все вхождения
    ("hello", "x", "hello"),  # ничего не нашлось
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_negative_empty_symbol():
    """
    Если символ пустой "" — поведение неопределённое.
    replace("", "") ничего не делает или работает странно.
    Это дефект.
    """
    assert string_utils.delete_symbol("hello", "") == "hello"


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
    ("hello", None),
    (123, "1"),
])
def test_delete_symbol_negative_wrong_type(string, symbol):
    with pytest.raises(Exception):
        string_utils.delete_symbol(string, symbol)
