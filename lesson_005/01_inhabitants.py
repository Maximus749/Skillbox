# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

# room_1.folks[0]
print("В комнате room_1 живут: ", end="")
for folk in room_1.folks:
    print(folk, end=", ")
print()
print("В комнате room_2 живут: ", end="")
for folk in room_2.folks:
    print(folk)

