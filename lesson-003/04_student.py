# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

monthes = 0
needed_amount_of_money = 0
monthly_diference = 0
while monthes < 10:
    if monthes > 0:
        expenses = expenses * 1.03
    monthly_diference = expenses - educational_grant
    needed_amount_of_money += monthly_diference
    monthes += 1
    print( monthes, monthly_diference, needed_amount_of_money)
print("Студенту надо попросить", round(needed_amount_of_money, 2), "рублей")