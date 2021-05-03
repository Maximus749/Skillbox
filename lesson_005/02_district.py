# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import pprint
from district.central_street.house1 import room1 as CT11
from district.central_street.house1 import room2 as CT12
from district.central_street.house2 import room1 as CT21
from district.central_street.house2 import room2 as CT22
from district.soviet_street.house1 import room1 as ST11
from district.soviet_street.house1 import room2 as ST12
from district.soviet_street.house2 import room1 as ST21
from district.soviet_street.house2 import room2 as ST22

print("На районе живут: ", end=" ")
for folk in CT11.folks:
    print(folk, end=" ")
print()
for folk in CT12.folks:
    print(folk, end=" ")
print()
for folk in CT21.folks:
    print(folk, end=" ")
print()
for folk in CT22.folks:
    print(folk, end=" ")
print()
for folk in ST11.folks:
    print(folk, end=" ")
print()
for folk in ST12.folks:
    print(folk, end=" ")
print()
for folk in ST21.folks:
    print(folk, end=" ")
print()
for folk in ST22.folks:
    print(folk, end=" ")



