import decimal


class SimpleCalculator:
    def __init__(self):
        self.answer = 0
        self.last_number = []

    def __str__(self):
        return f'{self.answer} | {self.last_number}'

    def prev_numb(self):
        # saves curent number for going back if needed
        self.last_number.append(self.answer)

    def go_back(self):
        # gives previous result
        try:
            self.answer = self.last_number.pop()
        except IndexError:
            self.answer = 0

    def clear(self):
        # reset
        self.answer, self.last_number = 0, []

    def addition(self, add_numb):
        self.prev_numb()
        self.answer += add_numb
        return self.answer

    def subtraction(self, sub_numb):
        self.prev_numb()
        self.answer -= sub_numb
        return self.answer

    def multiplication(self, by_numb):
        self.prev_numb()
        self.answer *= by_numb
        return self.answer

    def division(self, by_numb):
        self.prev_numb()
        try:
            self.answer /= by_numb
        except ZeroDivisionError:
            print(f"Don't divide by zero!")
        return self.answer

    def to_the_second_power(self):
        self.prev_numb()
        self.answer = self.answer * self.answer
        return self.answer

    def to_the_power_of(self, numb):
        self.prev_numb()
        self.answer = self.answer ** numb
        return self.answer

    def square_root_of_two(self):
        self.prev_numb()
        try:
            self.answer = decimal.Decimal(self.answer).sqrt()
        except decimal.InvalidOperation:
            print('It is impossible to find the square root of negative one')
        return self.answer


def get_number(number):
    try:
        val = int(number)
        return val
    except ValueError:
        try:
            val = float(number)
            return val
        except ValueError:
            print("Only numbers for value")


def helping_hand():
    help_me = [['add', '+', 'substract', '-'], ['multiply', '*', 'divide', '/'],
               ['to the 2 power', '^2', 'to the power of x', '^'], ['square root', '//'],
               ['go back', 'b', 'clear everything', 'c']]
    col_width = max(len(word) for row in help_me for word in row) + 2
    for row in help_me:
        print("".join(word.ljust(col_width) for word in row))


# save i przypomnienie

alpha = SimpleCalculator()

if __name__ == '__main__':
    helping_hand()
    while True:
        print(alpha.answer)
        if alpha.answer == 0:
            num = input('Enter your value:')
            value = get_number(num)
            if value is None:
                continue
            alpha.answer = value
            continue
        operation = input('Choose operation sign +, -, *, ^2, ^, /, //2, \n'
                          'c for clear, b to go back, h for help, exit to stop the program:')
        if operation not in ['+', '-', '*', '/', ]:
            if operation == '^2':
                alpha.to_the_second_power()
                continue
            elif operation == '^':
                num = input('Number to the power of:')
                value = get_number(num)
                alpha.to_the_power_of(value)
                continue
            elif operation == '//':
                alpha.square_root_of_two()
                continue
            elif operation == 'b':
                alpha.go_back()
                continue
            elif operation == 'c':
                alpha.clear()
                continue
            elif operation == 'h':
                helping_hand()
                continue
            elif operation == 'exit':
                break
            print('Wrong operator')
            continue

        num = input('Enter your value:')
        value = get_number(num)

        if value is None:
            continue

        if operation == '+':
            alpha.addition(value)
        elif operation == '-':
            alpha.subtraction(value)
        elif operation == '*':
            alpha.multiplication(value)
        elif operation == '/':
            alpha.division(value)
