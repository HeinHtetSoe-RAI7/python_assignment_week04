addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "ERROR!"

def main():
    print(addition(5, 3))
    print(subtraction(10, 4))
    print(multiplication(2, 6))
    print(division(8, 2))

main()