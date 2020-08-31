what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5] }

what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("LOAD_VALUE", 1),
                         ("ADD_TWO_VALUES", None),
                         ("LOAD_VALUE", 2),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [7, 5, 8] }

# >>> def s():
# ...     a = 1
# ...     b = 2
# ...     print(a + b)
# a friendly compiler transforms `s` into:

what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [1, 2],
    "names":   ["a", "b"] }

#implement
#LOAD_VALUE
#ADD_TWO_VALUES
#PRINT_ANSWER

class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def LOAD_VALUE(self,number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_number = self.stack.pop()
        second_number = self.stack.pop()
        total = first_number + second_number
        self.stack.append(total)

    def STORE_NAME(self,variable):
        val = self.stack.pop()
        self.environment[variable] = val

    def LOAD_NAME(self,variable):
        val = self.environment[variable]
        self.stack.append(val)

    def parse_argument(self,instruction, argument, what_to_execute):
        """ Understand what the argument to each instruction means."""
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME","STORE_NAME"]
        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        elif instruction in names:
            argument = what_to_execute["names"][argument]
        return argument

    def run_code(self,what_to_execute):
        instructions = what_to_execute['instructions']
        for each_step in instructions:
            instruction,argument = each_step
            argument = self.parse_argument(instruction,argument,what_to_execute)
            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)
            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(argument)

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)