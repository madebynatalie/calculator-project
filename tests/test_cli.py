from unittest.mock import patch
from calculator.cli import get_number, main


def test_get_number_valid_input():
    with patch("builtins.input", return_value="5"):
        assert get_number("Enter number: ") == 5.0


def test_get_number_invalid_then_valid_input():
    with patch("builtins.input", side_effect=["abc", "10"]):
        assert get_number("Enter number: ") == 10.0


def test_main_quit(capsys):
    with patch("builtins.input", side_effect=["quit"]):
        main()

    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out


def test_main_invalid_operation(capsys):
    with patch("builtins.input", side_effect=["power", "quit"]):
        main()

    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out


def test_main_addition(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "5", "3", "quit"]
    ):
        main()

    captured = capsys.readouterr()
    assert "Result: 8.0" in captured.out


def test_main_divide_by_zero(capsys):
    with patch(
        "builtins.input",
        side_effect=["divide", "5", "0", "quit"]
    ):
        main()

    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out