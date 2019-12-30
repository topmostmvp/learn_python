import unittest
from employee import Employee

class Test_employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('aa','cc', 5000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(10000, self.employee.rise)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(6000, self.employee.rise)

unittest.main()