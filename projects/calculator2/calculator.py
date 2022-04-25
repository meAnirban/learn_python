class Calculator:

    def __init__(self):
        self.num1 = float(input("Enter your first number :"))
        self.num2 = float(input("Enter your second number :"))

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
    operator = Calculator()
    operator.add()
    operator.subtract()
    operator.multiply()
    operator.divide()