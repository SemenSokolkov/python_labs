import person
class Client(person.Person):
    def __init__(self, surname : str = "NOVALUE", name : str = "NOVALUE", patronymic : str = "NOVALUE", age : int = 0, order : str = "NOVALUE"):
        super().__init__(surname, name, patronymic, age);
        self.order = order;

    def __str__(self) -> str:
        return super().__str__() + f"\tЗаказ: {self.order}";

    def __repr__(self)-> str:
        return "Client: " + self.__str__();