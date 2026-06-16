# Design an Employee System

Practice **inheritance** in object-oriented programming.

## Problem

Design a small system for different types of employees.

There is a general `Employee`, and there are three specific employee types:

- `FullTimeEmployee`
- `PartTimeEmployee`
- `Intern`

Each employee has some common information, but each employee type calculates monthly pay differently.

## Core Requirements

Every employee should have:

```text
employee_id
name
```

Every employee should support:

```text
get_id()
get_name()
get_role()
calculate_monthly_pay()
```

Specific behavior:

```text
FullTimeEmployee:
- Has a fixed monthly salary.
- calculate_monthly_pay() returns that salary.

PartTimeEmployee:
- Has hourly wage and hours worked.
- calculate_monthly_pay() returns hourly_wage * hours_worked.

Intern:
- Has a fixed stipend.
- calculate_monthly_pay() returns the stipend.
```

## Task

Implement:

```text
1. A base class Employee.

2. Three child classes:
   - FullTimeEmployee
   - PartTimeEmployee
   - Intern

3. Common fields should be stored in Employee.

4. Type-specific fields should be stored in the child classes.

5. Common methods should be implemented in Employee.

6. Type-specific behavior should be implemented in the child classes.

7. Write a small main/test section that:
   - creates one FullTimeEmployee
   - creates one PartTimeEmployee
   - creates one Intern
   - prints each employee's id, name, role, and monthly pay
```

---

## Expected Class Design

```text
Employee
├── FullTimeEmployee
├── PartTimeEmployee
└── Intern
```

### `Employee`

```text
Fields:
    employee_id
    name

Methods:
    get_id()
    get_name()
    get_role()
    calculate_monthly_pay()
```

### `FullTimeEmployee` extends `Employee`

```text
Fields:
    monthly_salary

Methods:
    get_role()
    calculate_monthly_pay()
```

### `PartTimeEmployee` extends `Employee`

```text
Fields:
    hourly_wage
    hours_worked

Methods:
   get_role()
    calculate_monthly_pay() 
```

### `Intern` extends `Employee`

```text
Fields:
    stipend

Methods:
    get_role()
    calculate_monthly_pay()
```

---

## Main Inheritance Idea

* Common fields go in the parent class.
* Different fields go in the child classes.
* Common methods can go in the parent class.
* Different behavior can be implemented in the child classes.

Example:

* `employee_id` and `name` are common to all employees,
so they belong in `Employee`.
* `monthly_salary` only applies to `FullTimeEmployee`,
so it belongs in `FullTimeEmployee`.
* `hourly_wage` and `hours_worked` only apply to `PartTimeEmployee`, so they belong in `PartTimeEmployee`.
* `stipend` only applies to `Intern`, so it belongs in `Intern`.