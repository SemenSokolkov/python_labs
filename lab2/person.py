class Person:
    def __init__(self, surname : str = "NOVALUE", name : str = "NOVALUE", patronymic : str = "NOVALUE", age : int = 0):
        self.surname = surname;
        self.name = name;
        self.patronymic = patronymic;
        self.age = age;


    def __str__(self) -> str:
        return f"ФИО: {self.surname} {self.name} {self.patronymic}\tвозраст: {self.age}";


    def __repr__(self)-> str:
        return "Person: " + self.__str__();