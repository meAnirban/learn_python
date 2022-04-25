import argparse

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        sum = self.num1 + self.num2
        print(f"Summation of {self.num1} and {self.num2} = {sum}")
        return sum

    def subtract(self):
        sub = self.num1 - self.num2
        print(f"Subtraction of {self.num1} and {self.num2} = {sub}")
        return sub

    def multiply(self):
        mul = self.num1 * self.num2
        print(f"Multiplication of {self.num1} and {self.num2} = {mul}")
        return mul

    def divide(self):
        div = self.num1 / self.num2
        print(f"division of {self.num1} and {self.num2} = {div}")
        return div


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'calculator arguments')

    parser.add_argument('-num1', '--number1', required = True, type = float, help='Enter your first number ')
    parser.add_argument('-num2', '--number2', required = True, type = float, help='Enter your second number ')

    args = parser.parse_args()

    operator = Calculator(args.number1, args.number2)
    operator.add()
    operator.subtract()
    operator.multiply()
    operator.divide()