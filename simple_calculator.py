from math import sqrt
import math
class SimpleCalculator:
    def __init__(self):
        self.answer = 0
        self.last_number = [0]

    def __str__(self):
        return f'{self.answer} | {self.last_number}'

    def prev_numb(self):
        self.last_number.append(self.answer)

    def go_back(self):
        try:
            self.answer = self.last_number.pop()
        except IndexError:
            self.answer = 0

    def clear(self):
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
        self.answer = sqrt(self.answer)
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


# save i przypomnienie

alpha = SimpleCalculator()

while True:
    print(alpha.answer)
    if alpha.answer == 0:
        num = input('Enter your value:')
        value = get_number(num)
        print("hello")
        alpha.answer = value
        continue
    operation = input('Choose mathematical operation sign + - * / ** :')
    if operation not in ['+', '-', '*', '/']:
        if operation == 'b':
            alpha.go_back()
            continue
        elif operation == 'c':
            alpha.clear()
            continue
        elif operation == '**':
            alpha.to_the_second_power()
            continue
        elif operation == '***':
            num = input('Enter your value:')
            value = get_number(num)
            alpha.to_the_power_of(value)
            continue
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
