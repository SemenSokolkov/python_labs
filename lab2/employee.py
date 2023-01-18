import person
class Employee(person.Person):
    def __init__(self, surname : str = "NOVALUE", name : str = "NOVALUE", patronymic : str = "NOVALUE", age : int = 0, salary : int = 0):
        super().__init__(surname, name, patronymic, age);
        self.salary = salary;

    def  __str__(self) -> str:
        return super().__str__() + f"\tДоход: {self.salary}";

    def __repr__(self)-> str:
        return "Employee: " + self.__str__();