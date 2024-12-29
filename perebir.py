import time


def discrete_log_brute_force(A, B, n, max_time):
    start_time = time.time()
    for x in range(n):
        if pow(A, x, n) == B:
            return x
        if time.time() - start_time > max_time:
            print("Час вичерпано, рішення не знайдено.")
            return None
    print("Рішення не знайдено в межах можливих значень.")
    return None

A = int(input("Введіть генератор: "))
B = int(input("Введіть елемент групи: "))
n = int(input("Введіть порядок групи: "))

max_time = 300  # 5 хвилин

x = discrete_log_brute_force(A, B, n, max_time)
if x is not None:
    print(f"Знайдено розв'язок: x = {x}")
else:
    print("Розв'язок не знайдено.")
