import unittest
from practice import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.original_income = 400000
        self.employee = Employee('yu', 'yang', self.original_income)
        self.custome_increments = 1000

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.income, self.original_income + 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(self.custome_increments)
        self.assertEqual(self.employee.income, self.original_income + self.custome_increments)

unittest.main()