def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(add(num1, num2))
    print(subtract(num1, num2))
    print(multiply(num1, num2))
    try:
        print(divide(num1, num2))
    except ValueError as e:
        print(e)
