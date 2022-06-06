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

    def expression_valid(self, expression):
        # It's a command
        if expression[0].startswith("/"):
            return True
        # Last operator must be just a number, without any operation after
        try:
            num = int(expression[-1])
        except ValueError:
            return False
        # Check if there are consecutive operators without operation in between
        if len(expression) > 1:
            for op in expression[1::2]:
                if self.operator_sign(op) not in self.operations:
                    return False
        # Valid if no invalid conditions found
        return True

    def run(self):
        while True:
            user_input = input().split()
            # Input empty
            if not len(user_input):
                continue
            if not self.expression_valid(user_input):
                print("Invalid expression")
                continue
            # Length 1 expression
            if len(user_input) == 1:
                if user_input[0] == "/help":
                    print("The program calculates expressions with '+' and '-'")
                elif user_input[0] == "/exit":
                    print("Bye!")
                    break
                elif user_input[0].startswith("/"):
                    print("Unknown command")
                else:
                    # Only one number as input
                    print(int(user_input[0]))
            # Length >1 expression
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
