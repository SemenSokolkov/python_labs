import csv;
import random;
FILENAME : str = "data_set.csv"; #имя изначального файла с данными
OUTPUTFILE : str = "new_data_set.csv"; #имя преобразованного файла с данными

#переопределённый map
def OverrideMap(func, sourceList : list) -> list:
    resultList = list();
    for obj in sourceList:
        resultList.append(func(obj));
    return resultList;

#переопределённый reduce
def OverrideReduce(func, sourceList : list):
    index : int = 2;
    length : int = len(sourceList);
    result = func(sourceList[0], sourceList[1]);
    while(index < length):
        result = func(result, sourceList[index]);
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
   
#Запись в .csv из списка списков
def WriteInCSVFromListList(dataSet : list, fileName : str):
     with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, delimiter=',');
        writer.writerows(dataSet);

#Запись в .csv из списка словарей        
def WriteInCSVFromListDict(dataSet : list, fileName : str):
    with open(fileName, "w", newline="") as file:
        columns = list(dataSet[0].keys());
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader();   
        writer.writerows(dataSet);

#Чтение из .csv в виде списка словарей
def ReadFromCSV(fileName : str) -> list:
    with open(fileName, "r", newline="") as file:
        reader = csv.DictReader(file);
        resultListDict = list();
        for dict in reader:
            resultListDict.append(dict);        
    return resultListDict;

def SplitFullNameFromDict(sourceDict : dict) -> dict:
    resultDict = dict();
    strs = sourceDict["ФИО"].split(' ');
    resultDict["Фамилия"] = strs[0];
    resultDict["Имя"] = strs[1];
    resultDict["Отчество"] = strs[2];
    resultDict["Зарплата"] = sourceDict["Зарплата"];
    return resultDict;

#Генерация изначального файла .csv
WriteInCSVFromListList(GenerateDataSet(), FILENAME);

#Задача 1, разрезать столбец ФИО на отдельные столбцы и записать в новый файл .csv
dataSet : list = ReadFromCSV(FILENAME);
newDataSet : list = OverrideMap(SplitFullNameFromDict, dataSet);
WriteInCSVFromListDict(newDataSet, OUTPUTFILE);