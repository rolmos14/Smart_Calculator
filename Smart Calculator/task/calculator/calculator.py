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
        while True:
            user_input = input().split()
            if not len(user_input):
                continue
            elif len(user_input) == 1:
                if user_input[0] == "/exit":
                    print("Bye!")
                    break
                else:
                    print(*user_input)
            else:
                operator_1, operator_2 = [int(op) for op in user_input]
                self.result = self.addition(operator_1, operator_2)
                print(self.result)


calculator = SmartCalculator()
calculator.run()
