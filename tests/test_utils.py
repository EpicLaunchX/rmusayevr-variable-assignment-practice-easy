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
