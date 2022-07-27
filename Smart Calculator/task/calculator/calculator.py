class SmartCalculator:

    operations = ('*', '/', '+', '-')

    def __init__(self):
        self.result = 0
        self.variables = {}
        self.expression = ""

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

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
        return "="

    def expression_valid(self, expression):
        expression_split = expression.split()
        # Check there is no operation at the end
        if any(operation in expression[-1] for operation in self.operations):
            return False
        # Check if there are consecutive operators without operation in between
        for op in expression_split[1::2]:
            if self.operator_sign(op) not in self.operations:
                return False
        # Check all operators are either numbers or valid variables
        for op in expression_split[::2]:
            if self.identifier_valid(op) or self.number_valid(op):
                continue
            else:
                return False
        # Valid if no invalid conditions found
        return True

    def number_valid(self, num: 'str') -> 'True if num is valid number':
        return num.isnumeric()

    def identifier_valid(self, id: 'str') -> 'True if id contains only letters':
        return id.isalpha()

    def get_variable_value(self, var_name) -> 'Variable numeric value':
        var_value = self.variables[var_name]
        # Keep searching for variable value until it is a number
        while True:
            if self.number_valid(var_value):
                return var_value
            else:
                var_value = self.variables[var_value]

    def parse_expression(self, expression: 'str') -> 'string indicating expression type: ' \
                                                     'cmd/var/assign/calc/assign_calc':
        self.expression = expression
        # It's a command
        if self.expression.startswith("/"):
            return "cmd"
        if "=" not in self.expression:
            # It's a calculation
            if any(operation in self.expression for operation in self.operations):
                return "calc"
            # It's a variable identifier
            return "var"
        # It's a variable assignment without calculation
        assignment = self.expression.split("=")[1].strip()
        if assignment and not any(operation in assignment for operation in self.operations):
            return "assign"
        # It's a variable assignment with calculation
        return "assign_calc"

    def command(self) -> 'False if /exit command; otherwise True':
        """
        Executes known commands.
        """
        if self.expression == "/help":
            print("Input a variable followed by an assignment if desired. The assignment can be "
                  "an operation with '+' and '-'")
        elif self.expression == "/exit":
            print("Bye!")
            return False
        elif self.expression.startswith("/"):
            print("Unknown command")
        return True

    def variable(self):
        """
        Prints variable value if it exists; 'Unknown variable' if it doesn't exist; 'Invalid identifier' if variable
        syntax is not valid (only letters are allowed).
        """
        if self.identifier_valid(self.expression):
            try:
                print(self.get_variable_value(self.expression))
            except KeyError:
                print("Unknown variable")
        else:
            print("Invalid identifier")

    def variable_assignment(self):
        """
        Assign value to variable if both variable and assignment are valid.
        """
        variable, assignment = self.expression.split("=", 1)
        # Remove spaces in variable and assignment
        variable = variable.strip()
        assignment = assignment.strip()
        if self.identifier_valid(variable):
            if self.number_valid(assignment) or self.identifier_valid(assignment):
                if self.number_valid(assignment) or assignment in self.variables:
                    self.variables[variable] = assignment
                else:
                    print("Unknown variable")
            else:
                print("Invalid assignment")
        else:
            print("Invalid identifier")

    def calculation(self, expression) -> 'True if calculation could be performed':
        """
        Performs calculation and stores result.
        """
        self.result = 0
        if not self.expression_valid(expression):
            print("Invalid expression")
            return False
        else:
            expression_split = expression.split()
            first_op = expression_split[0]
            if self.number_valid(first_op):
                self.result = int(first_op)
            elif self.identifier_valid(first_op):
                if first_op in self.variables:
                    self.result = int(self.get_variable_value(first_op))
                else:
                    print("Unknown variable")
                    return False
            else:
                print("Invalid identifier")
                return False
            for idx in range(1, len(expression_split), 2):
                op_sign = self.operator_sign(expression_split[idx])
                next_op = expression_split[idx + 1]
                if self.number_valid(next_op):
                    next_op = next_op
                elif self.identifier_valid(next_op):
                    if next_op in self.variables:
                        next_op = self.get_variable_value(next_op)
                    else:
                        print("Unknown variable")
                        return False
                else:
                    print("Invalid identifier")
                    return False
                if op_sign == '+':
                    self.result = self.addition(self.result, int(next_op))
                elif op_sign == '-':
                    self.result = self.subtraction(self.result, int(next_op))
        return True

    def assign_calculation(self):
        """
        Assign calculation to variable if both variable and calculation are valid.
        """
        variable, assignment = self.expression.split("=", 1)
        # Remove spaces in variable and assignment
        variable = variable.strip()
        assignment = assignment.strip()
        if self.identifier_valid(variable):
            if self.expression_valid(assignment):
                if self.calculation(assignment):
                    self.variables[variable] = self.result
            else:
                print("Invalid assignment")
        else:
            print("Invalid identifier")

    def run(self):
        while True:
            user_input = input()
            # Input empty
            if not len(user_input):
                continue
            # Parse expression
            expression_type = self.parse_expression(user_input)
            # Execute command
            if expression_type == "cmd":
                if self.command():
                    continue
                else:
                    break
            # Show variable
            if expression_type == "var":
                self.variable()
                continue
            # Variable assignment, no calculation
            if expression_type == "assign":
                self.variable_assignment()
                continue
            # Calculation, no variable assignment
            if expression_type == "calc":
                if self.calculation(self.expression):
                    print(self.result)
                continue
            # Variable assignment & calculation
            if expression_type == "assign_calc":
                self.assign_calculation()
                continue


calculator = SmartCalculator()
calculator.run()
