def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("ERROR!")
    return x / y

def main():
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(2, 6))
    print(divide(8, 2))

main()