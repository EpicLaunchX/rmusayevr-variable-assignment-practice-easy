from src.pytemplate.utils import variables_example


def test_my_int():
    assert isinstance(variables_example.my_int, int)
    assert variables_example.my_int == 19


def test_my_str():
    assert isinstance(variables_example.my_str, str)
    assert variables_example.my_str == "epiclaunchx"


def test_my_float():
    assert isinstance(variables_example.my_float, float)
    assert variables_example.my_float == 3.14


def test_print_variables_output(capsys):
    global variables_example

    variables_example.my_int = 1
    variables_example.my_str = "x"
    variables_example.my_float = 2.5

    variables_example.print_variables()

    captured = capsys.readouterr()
    assert "my_int: 1" in captured.out
    assert "my_str: x" in captured.out
    assert "my_float: 2.5" in captured.out
