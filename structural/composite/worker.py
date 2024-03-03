from i_employee import IEmployee


class Worker(IEmployee):
    def display(self, indent: int):
        print(f"{'-' * indent} {self.name} - {self.salary}")