a: int = 5
b: int = 10

sum_ab: int = a + b
product_ab: int = a * b


def calculate_and_print(a, b) -> None:
    sum_ab = a + b
    product_ab = a * b
    print(f"Sum of a and b: {sum_ab}")
    print(f"Product of a and b: {product_ab}")
