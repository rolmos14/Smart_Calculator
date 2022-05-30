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

    def subtraction(self, a, b):
        return a - b

    def operator_sign(self, operator):
        if '+' in operator:
            return '+'
        if '-' in operator:
            if len(operator) % 2 != 0:
                return '-'
            else:
                return '+'

    def run(self):
        while True:
            user_input = input().split()
            if not len(user_input):
                continue
            elif len(user_input) == 1:
                if user_input[0] == "/help":
                    print("The program calculates expressions with '+' and '-'")
                elif user_input[0] == "/exit":
                    print("Bye!")
                    break
                else:
                    print(*user_input)
            else:
                self.result = int(user_input[0])
                for idx in range(1, len(user_input), 2):
                    op_sign = self.operator_sign(user_input[idx])
                    if op_sign == '+':
                        self.result = self.addition(self.result, int(user_input[idx + 1]))
                    elif op_sign == '-':
                        self.result = self.subtraction(self.result, int(user_input[idx + 1]))
                print(self.result)


calculator = SmartCalculator()
calculator.run()
