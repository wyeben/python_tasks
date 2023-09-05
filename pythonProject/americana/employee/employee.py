class Employee:
    emp_id = 0

    def __init__(self, emp_name: str, emp_department: str):
        self.emp_id += 1
        self.emp_name = emp_name
        self.emp_salary = 0.0
        self.emp_department = emp_department
        self.hourly_rate = 10.0
        self.number_of_hours_worked = 0

    def calculate_emp_salary(self, number_of_hours_worked: int):
        if number_of_hours_worked <= 0:
            print("Need a valid number of hours worked.")
        else:
            self.number_of_hours_worked = number_of_hours_worked
            self.emp_salary = self.hourly_rate * number_of_hours_worked

    def emp_assign_department(self, department: str):
        self.emp_department = department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary:.2f}")
        print(f"Employee Department: {self.emp_department}")
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Number of Hours Worked: {self.number_of_hours_worked} hours")
