from datetime import datetime, timedelta

# 1
now = datetime.today()
five_days_ago = now - timedelta(days=5)
print("5 дней назад:", five_days_ago.date())

# 2
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
print("Вчера:", yesterday.date())
print("Сегодня:", now.date())
print("Завтра:", tomorrow.date())

# 3
now_without_microseconds = datetime.now().replace(microsecond=0)
print("Без микросекунд:", now_without_microseconds)

# 4
date1 = datetime(2024, 2, 20, 12, 0, 0)
date2 = datetime(2024, 2, 25, 14, 30, 0)
diff_seconds = (date2 - date1).total_seconds()
print("Разница в секундах:", int(diff_seconds))

# 5
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

# 6
n = int(input("Введите число n: "))
even_numbers = (str(i) for i in range(0, n + 1, 2))
print(", ".join(even_numbers))

# 7
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 8
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for sq in squares(2, 5):
    print("Квадрат числа:", sq)

# 9
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print("Обратный отсчет:", num)
