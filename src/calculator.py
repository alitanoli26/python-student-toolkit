"""Small CLI calculator demonstrating validation and function dispatch."""

from operator import add, sub, mul, truediv

OPERATIONS = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculate(left: float, operator: str, right: float) -> float:
    if operator not in OPERATIONS:
        raise ValueError("Unsupported operator")
    if operator == "/" and right == 0:
        raise ValueError("Cannot divide by zero")
    return OPERATIONS[operator](left, right)


def main() -> None:
    print("Python Student Toolkit / Calculator")
    try:
        left = float(input("First number: "))
        operator = input("Operator (+ - * /): ").strip()
        right = float(input("Second number: "))
        print(f"Result: {calculate(left, operator, right):g}")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
