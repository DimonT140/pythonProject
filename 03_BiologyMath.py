# Тестер
s = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print(s)
print("          Тест \"БИОЛОГИЯ + МАТЕМАТИКА\"")
print(s)
prav = 0  # Счётчик правильных ответов
print("В тесте 5 вопросов. Ответы - числа.")
input("Готовы? Нажмите Enter.")
print("Вопрос 1.")
otv = int(input("Сколько лапок у 7 тараканов? "))
if otv == 42:
    prav += 1  # это то же самое, что prav = prav + 1
print("Вопрос 2.")
otv = int(input("У скольких кошек лап на 9 больше, чем хвостов? "))
if otv == 3:
    prav += 1
print("Вопрос 3.")
otv = int(input("Комариха выполняет укус каждые 5 минут.\nСколько укусов она произведёт за 3 часа? "))
if otv == 36:
    prav += 1
print("Вопрос 4.")
otv = int(input("За неделю трава на газоне вырастает на 42 мм.\nНа сколько мм вырастает трава за 10 дней? "))
if otv == 60:
    prav += 1
print("Вопрос 5.")
otv = int(input(
    "Количество микробов в пробирке удваивается ежеминутно.\nСейчас там один микроб.\nЧерез сколько минут там будет больше 1000 микробов? "))
if otv == 10:
    prav += 1
print("Количество правильных ответов:", prav)
