"""Напишіть програму, у якій користувач вводить значення поточної
дати: день, місяць і рік (цілі числа), а програма виводить вчорашню дату у
форматі: дд.мм.рррр.
Голомоза Інна Андріївна"""

# Введення даних
day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))
year = int(input("Введіть рік: "))

leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) # Перевірка високосного року

if not(1 <= day <= 31) or not (1 <= month <= 12) or year < 1: #Перевірка чи коректні дані
    print("Введені дані некоректні.")
else:    
    day -= 1
    if day == 0:
        month -= 1
    if month == 0:
        month = 12
        year -= 1
    if day == 0:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = 30
        else:
            if leap_year:
                day = 29
            else:
                day = 28
                    
    # Виведення результату
    print(f"Вчорашня дата: {day:02d}.{month:02d}.{year:04d}")
   

