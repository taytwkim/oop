#include <iostream>
#include <string>

class Employee {
/*
 * public:
 *      Anyone can access it.
 *s
 * private:
 *      Only member functions of this class can access it.
 *
 * protected:
 *      Member functions of this class can access it.
 *      Child classes can also access it.
 *      Outside code cannot access it directly.
 */
protected:
    std::string employee_id;
    std::string name;

public:
    Employee(std::string employee_id, std::string name)
        : employee_id(employee_id), name(name) {}

    // This const after the function name means that the method
    // will not modify the object it is called on.
    // This specific form of const is used for class member functions.
    std::string get_id() const {
        return employee_id;
    }

    std::string get_name() const {
        return name;
    }

    /*
    * virtual means when this method is called through a
    * parent pointer/reference, C++ should use the child class version
    * if the actual object is a child object.
    *
    * For example:
    *      Employee* e = new FullTimeEmployee("E1", "Alice", 5000);
    *
    * Here, the pointer type is Employee*,
    * but the actual object is FullTimeEmployee.
    *
    * virtual ensures that overridden child methods are called.
    */
    virtual std::string get_role() const {
        return "Employee";
    }

    virtual int calculate_monthly_pay() const {
        return 0;
    }

    /* ~Employee() is a destructor for Employee
     * 
     * A destructor runs when an object is destroyed.
     * 
     * For example, we can do something like: 
     * 
     * ~Employee() {
     *      std::cout << "Employee destroyed\n";
     * }
     * 
     * The virtual keyword ensures that the child object's 
     * destructor runs when it is deleted through a parent pointer.
     * 
     * default means use the default destructor.
     */
    virtual ~Employee() = default;
};

/*
 * public here means the child class can be treated
 * as an instance of the parent class by outside code.
 *
 * For example:
 *      FullTimeEmployee is an Employee.
 *
 * So this is allowed:
 *      Employee* p = new FullTimeEmployee(...);
 *      Employee& r = full_time_employee;
 *
 * C++ also supports private inheritance:
 *      class Child : private Parent
 *
 * With private inheritance, the child still reuses the parent
 * internally, but outside code cannot treat the child as a parent.
 *
 * So this would not be allowed:
 *      Parent* p = new Child(...);
 *
 * For normal OOP "is-a" relationships and polymorphism,
 * we almost always use public inheritance.
 */
class FullTimeEmployee : public Employee {
private:
    int monthly_salary;

public:
    FullTimeEmployee(std::string employee_id, std::string name, int monthly_salary)
        : Employee(employee_id, name), monthly_salary(monthly_salary) {}

    std::string get_role() const override {
        return "Full-Time Employee";
    }

    int calculate_monthly_pay() const override {
        return monthly_salary;
    }
};

class PartTimeEmployee : public Employee {
private:
    int hourly_wage;
    int hours_worked;

public:
    PartTimeEmployee(std::string employee_id, std::string name, int hourly_wage, int hours_worked)
        : Employee(employee_id, name), hourly_wage(hourly_wage), hours_worked(hours_worked) {}

    std::string get_role() const override {
        return "Part-Time Employee";
    }

    int calculate_monthly_pay() const override {
        return hourly_wage * hours_worked;
    }

    void add_hours(int hours) {
        hours_worked += hours;
    }
};

class Intern : public Employee {
private:
    int stipend;

public:
    Intern(std::string employee_id, std::string name, int stipend)
        : Employee(employee_id, name), stipend(stipend) {}

    std::string get_role() const override {
        return "Intern";
    }

    int calculate_monthly_pay() const override {
        return stipend;
    }
};

void print_employee_info(const Employee& employee) {
    std::cout << "ID: " << employee.get_id() << "\n";
    std::cout << "Name: " << employee.get_name() << "\n";
    std::cout << "Role: " << employee.get_role() << "\n";
    std::cout << "Monthly Pay: " << employee.calculate_monthly_pay() << "\n";
    std::cout << "\n";
}

int main() {
    FullTimeEmployee e1("E1", "Alice", 5000);
    PartTimeEmployee e2("E2", "Bob", 25, 80);
    Intern e3("E3", "Charlie", 1200);

    print_employee_info(e1);
    print_employee_info(e2);
    print_employee_info(e3);

    e2.add_hours(10);

    std::cout << "After adding 10 hours to Bob:\n";
    print_employee_info(e2);

    return 0;
}