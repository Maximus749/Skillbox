#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Наташа', 'Максим', 'Александра', 'Кирилл']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Мать Наташа', 170],
    ['Отец Максим', 180],
    ['Дочь Александра', 168],
    ['Сын Кирилл', 105]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[1][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Общий рост моей семьи -',
      my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1], 'см')
