"""Task 1: Python fundamentals, OOP, exceptions, and loops."""


class InvalidSalaryError(Exception):
    """Raised when an employee has a negative salary."""


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name} - {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()} - Team size: {self.team_size}"


def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)
    if "cap" in options:
        result = min(result, options["cap"])
    return result


def main():
    employees = [
        {"name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
        {"name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
        {"name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
        {"name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
        {"name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
        {"name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
        {"name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
        {"name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"},
    ]

    above_50000 = [e["name"] for e in employees if e["salary"] > 50000]
    raised = list(map(lambda e: e["salary"] * 1.10, employees))
    chennai = list(filter(lambda e: e["city"] == "Chennai", employees))
    chennai_names = [e["name"] for e in chennai]
    print("Above 50000:", above_50000)
    print("Chennai:", chennai_names)

    try:
        Employee("Test", -500)
    except InvalidSalaryError as exc:
        print("Error:", exc)
    finally:
        print("Transaction finished")

    for employee in employees:
        salary = employee["salary"]
        if salary == 0:
            continue
        if salary > 85000:
            break


if __name__ == "__main__":
    main()
