from pyDatalog import pyDatalog;
#Задание 2 (среднее значение ряда)
pyDatalog.create_terms('result, X');
result[X] = (1 + X) / 2;
print(result[100]==X);