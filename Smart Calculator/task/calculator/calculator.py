class SmartCalculator:

    operations = ('*', '/', '+', '-')

    def __init__(self):
        self.result = 0

    def multiplication(self):
        pass

    def division(self):
        pass

    def addition(self, a, b):
        return a + b

    def subtraction(self):
        pass

    def run(self):
        operator_1, operator_2 = [int(op) for op in input().split()]
        self.result = self.addition(operator_1, operator_2)
        print(self.result)


calculator = SmartCalculator()
calculator.run()
