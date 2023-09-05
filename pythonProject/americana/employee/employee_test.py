import unittest

from americana.employee.employee import Employee


class TestEmployee(unittest.TestCase):
    def test_calculate_emp_salary(self):
        emp = Employee("Americana", "singer")
        emp.calculate_emp_salary(40)
        self.assertEqual(emp.emp_salary, 400.0)

    def test_emp_assign_department(self):
        emp = Employee("ASA", "politician")
        emp.emp_assign_department("Governor")
        self.assertEqual(emp.emp_department, "Governor")

    def test_can_not_use_negative_salary(self):
        emp = Employee("Badboy", "419")
        emp.calculate_emp_salary(-40)
        self.assertEqual(emp.emp_salary, 0)

