import csv;
import random;
FILENAME : str = "data_set.csv"; #имя изначального файла с данными
OUTPUTFILE : str = "new_data_set.csv"; #имя преобразованного файла с данными
#переопределённый map
def OverrideMap(func, iterable : list) -> list:
    resultList = list();
    for obj in iterable:
        resultList.append(func(obj));
    return resultList;

#переопределённый reduce
def OverrideReduce(func, iterable : list):
    index : int = 2;
    length : int = len(iterable);
    result = func(iterable[0], iterable[1]);
    while(index < length):
        result = func(result, iterable[index]);
        index += 1;
    return result;

#Генерация списка списков с ФИО и зарплатой человека
def GenerateDataSet() -> list:
    Names : list = ["Денис", "Вячеслав", "Анатолий", "Олег", "Павел"];
    Surnames : list = ["Мельников", "Глазырин", "Омутных", "Гостев"];
    Patronymics : list = ["Денисович", "Вячеславович", "Анатольевич", "Олегович", "Павлович"];
    Persons = list();
    i : int = 0;
    count : int = 50;
    Persons.append(["ФИО", "Зарплата"]);
    while i < count:
        randomFullName = Surnames[random.randint(0 , len(Surnames) - 1)] + " " + Names[random.randint(0 , len(Names) - 1)] + " "  + Patronymics[random.randint(0 , len(Patronymics) - 1)];
        Persons.append([randomFullName, random.randint(1, 1000) * 1000]);
        i += 1;
    return Persons;
   
#Запись в .csv
def WriteInCSV(dataSet : list, fileName : str):
     with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, delimiter=',');
        writer.writerows(dataSet);

#основной код
WriteInCSV(GenerateDataSet(), FILENAME);