from i_employee import IEmployee


class Manager(IEmployee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.subordinates = []

    def add(self, employee: IEmployee):
        self.subordinates.append(employee)

    def remove(self, employee: IEmployee):
        self.subordinates.remove(employee)

    def display(self, indent: int):
        print(f"{'-' * indent} {self.name} - {self.salary}")
        for subordinate in self.subordinates:
            subordinate.display(indent + 2)