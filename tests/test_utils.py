from src.pytemplate.utils import expressions_example, variables_example


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


def test_sum_ab():
    assert isinstance(expressions_example.sum_ab, int)
    assert expressions_example.sum_ab == expressions_example.a + expressions_example.b
    assert expressions_example.sum_ab == 15


def test_product_ab():
    assert isinstance(expressions_example.product_ab, int)
    assert expressions_example.product_ab == expressions_example.a * expressions_example.b
    assert expressions_example.product_ab == 50


def test_calculate_and_print(capsys):
    global expressions_example
    expressions_example.a = 2
    expressions_example.b = 4

    expressions_example.calculate_and_print()

    captured = capsys.readouterr()
    assert "Sum of a and b: 6" in captured.out
    assert "Product of a and b: 8" in captured.out
