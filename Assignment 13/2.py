class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def getSalary(self):
        return f"{self.name}'s salary is {self.salary}."

class HRManager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        return f"{self.name} is managing human resources."

    def addEmployee(self, employee):
        return f"{self.name} has added {employee.name} as a new employee."

if __name__ == "__main__":
    emp1 = Employee("John", 50000)
    hr_manager = HRManager("Alice", 70000)

    print(emp1.work())
    print(emp1.getSalary())
    print(hr_manager.work())
    print(hr_manager.getSalary())
    print(hr_manager.addEmployee(emp1))