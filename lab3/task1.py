from pyDatalog import pyDatalog;
#Задание 1 (сумма ряда)
pyDatalog.create_terms('result, X');
result[X] = X + result[X-1];
result[1] = 1;
print(result[100]==X);