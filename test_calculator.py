import unittest
from calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.__calculations = SimpleCalculator()

    def test_go_back(self):
        self.__calculations.last_number = [16, 11, 213213, 9]
        self.__calculations.go_back()
        self.assertEqual(self.__calculations.answer, 9)
        self.assertEqual(self.__calculations.last_number, [16, 11, 213213])
        self.__calculations.go_back()
        self.assertEqual(self.__calculations.answer, 213213)
        self.assertEqual(self.__calculations.last_number, [16, 11])
        self.__calculations.go_back()
        self.assertEqual(self.__calculations.answer, 11)
        self.assertEqual(self.__calculations.last_number, [16])
        self.__calculations.go_back()
        self.assertEqual(self.__calculations.answer, 16)
        self.assertEqual(self.__calculations.last_number, [])
        self.__calculations.go_back()
        self.assertEqual(self.__calculations.answer, 0)
        self.assertEqual(self.__calculations.last_number, [])

    def test_addition(self):
        self.__calculations.addition(55)
        self.assertEqual(self.__calculations.answer, 55)
        self.assertEqual(self.__calculations.last_number, [0])
        self.__calculations.addition(5)
        self.assertEqual(self.__calculations.last_number, [0, 55])
        self.assertEqual(self.__calculations.answer, 60)

    def test_substraction(self):
        self.__calculations.subtraction(7)
        self.assertEqual(self.__calculations.answer, -7)
        self.__calculations.answer = 874319587
        self.__calculations.subtraction(4)
        self.assertEqual(self.__calculations.answer, 874319583)
        self.__calculations.subtraction(73248970)
        self.assertEqual(self.__calculations.answer, 801070613)
        self.assertEqual(self.__calculations.last_number, [0, 874319587, 874319583])

    def test_multiplication(self):
        self.__calculations.answer = 16
        self.__calculations.multiplication(16)
        self.assertEqual(self.__calculations.answer, 256)
        self.__calculations.answer = 11
        self.__calculations.multiplication(23)
        self.assertEqual(self.__calculations.answer, 253)
        self.__calculations.answer = 213213
        self.__calculations.multiplication(333216)
        self.assertEqual(self.__calculations.answer, 71045983008)

    def test_division(self):
        self.__calculations.answer = 16
        self.__calculations.division(16)
        self.assertEqual(self.__calculations.answer, 1)
        self.assertEqual(self.__calculations.last_number, [16])
        self.__calculations.answer = 11
        self.__calculations.division(3)
        self.assertEqual(self.__calculations.answer, 3.6666666666666665)
        self.assertEqual(self.__calculations.last_number, [16, 11])
        self.__calculations.answer = 213213
        self.__calculations.division(46)
        self.assertEqual(self.__calculations.answer, 4635.065217391304)
        self.assertEqual(self.__calculations.last_number, [16, 11, 213213])
        self.__calculations.answer = 99
        self.__calculations.division(9)
        self.assertEqual(self.__calculations.answer, 11)
        self.assertEqual(self.__calculations.last_number, [16, 11, 213213, 99])

    def test_to_the_second_power(self):
        self.__calculations.answer = 15
        self.__calculations.to_the_second_power()
        self.assertEqual(self.__calculations.answer, 225)
        self.__calculations.answer = 8
        self.__calculations.to_the_second_power()
        self.assertEqual(self.__calculations.answer, 64)
        self.assertEqual(self.__calculations.last_number, [15, 8])

    def test_to_the_power_of(self):
        self.__calculations.answer = 3
        self.__calculations.to_the_power_of(3)
        self.assertEqual(self.__calculations.answer, 27)
        self.__calculations.answer = 4
        self.__calculations.to_the_power_of(3)
        self.assertEqual(self.__calculations.answer, 64)

if __name__ == '__main__':
    unittest.main()
