import pytest

from calculator.operations import add, subtract, multiply, divide, calculate


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (1, 1, 0),
        (0, 5, -5),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


@pytest.mark.parametrize(
    "operation, a, b, expected",
    [
        ("add", 2, 2, 4),
        ("subtract", 5, 3, 2),
        ("multiply", 4, 3, 12),
        ("divide", 10, 2, 5),
    ],
)
def test_calculate(operation, a, b, expected):
    assert calculate(operation, a, b) == expected


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate("power", 2, 3)