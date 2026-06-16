class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def get_role(self):
        return "Employee"

    def calculate_monthly_pay(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def get_role(self):
        return "Full-Time Employee"

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_wage, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_role(self):
        return "Part-Time Employee"

    def calculate_monthly_pay(self):
        return self.hourly_wage * self.hours_worked

    # This method exists only in PartTimeEmployee.
    # It is not defined in the parent Employee class.
    def add_hours(self, hours):
        self.hours_worked += hours


class Intern(Employee):
    def __init__(self, employee_id, name, stipend):
        super().__init__(employee_id, name)
        self.stipend = stipend

    def get_role(self):
        return "Intern"

    def calculate_monthly_pay(self):
        return self.stipend


def print_employee_info(employee):
    print("ID:", employee.get_id())
    print("Name:", employee.get_name())
    print("Role:", employee.get_role())
    print("Monthly Pay:", employee.calculate_monthly_pay())
    print()


def main():
    e1 = FullTimeEmployee("E1", "Alice", 5000)
    e2 = PartTimeEmployee("E2", "Bob", 25, 80)
    e3 = Intern("E3", "Charlie", 1200)

    print_employee_info(e1)
    print_employee_info(e2)
    print_employee_info(e3)

    # Example of using a child-only method.
    # add_hours() only exists on PartTimeEmployee.
    e2.add_hours(10)

    print("After adding 10 hours to Bob:")
    print_employee_info(e2)


if __name__ == "__main__":
    main()