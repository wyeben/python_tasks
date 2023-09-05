from americana.employee.employee import Employee

employee1 = Employee("Americana", "label")
employee1.calculate_emp_salary(1000)
employee1.emp_assign_department("singer")
employee1.print_employee_details()

print("***************************")

employee2 = Employee("ASA", "Governor")
employee2.calculate_emp_salary(10000)
employee2.emp_assign_department("politician")
employee2.print_employee_details()
