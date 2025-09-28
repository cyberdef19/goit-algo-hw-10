"""
Очевидно, що на графіку бачимо майже трикутник,
побудований на обмежені кривої та прямої опущеної на x=2.0 і віссю OX.
Цей трикутник маємо змогу добудувати до прямокутника з обмеженням прямою на y=4 і
обмеженням прямою на 0.0. Якщо згенерувати для цього прямокутника N точок і помітити усі
точки, що потрапили в уявну фігуру обмежену кривою x**2 та прямою x=2.0 і віссю OX - їх буде M,
тоді певно площа цієї фігури буде складати:


S = M/N * Sпрям


де Sпрям - площа прямокутника


"""

import random
import scipy.integrate as spi


def is_inside_figure(x: float, y: float, a: float, b: float) -> bool:
    # x <= 2.0 та y >= 0.0
    return 0 <= x <= a and b <= y <= x ** 2


def random_range(number: int, a: float, b: float) -> list:
    # a = 2.0 - по X, b = 4.0 по Y
    return [(random.uniform(0, a), random.uniform(0, b)) for _ in range(number)]


def monte_carlo_integral(num_experiments, numbers):
    square_experiments = 0
    a = 2.0
    b = 4.0
    for _ in range(num_experiments):

        # Генеруємо точки
        points = random_range(numbers, a, b)
        # Масив точок, що потрапляє в поле фігури
        points_figure = [(x, y) for x, y in points if is_inside_figure(x, y, 2.0, 0.0)]

        # Кількість точок загальна
        N = len(points)
        # Кількість точок, що потрапили в зону фігури
        M = len(points_figure)

        # Площа прямокутника
        S = a * b
        # Площа фігури
        S_f = (M / N) * S

        # Збираємо значення усіх площ за кожен експеримент
        square_experiments += S_f

    # Визначаємо середню площу
    square_average = square_experiments / num_experiments

    print(f"За {num_experiments} експериментів")
    print(f"При кількості точок {numbers}")
    print(f"Площа фігури під кривою параболи {square_average}")
    return square_average


# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
mc_result = monte_carlo_integral(100, 1500)

print("Інтеграл за quad: ", result, error)
print("Інтеграл за Монте Карло: ", mc_result)

num_experiments = [100, 150, 500, 750, 1000]
numbers = [1500, 15000]

for experiment in num_experiments:
    for number in numbers:
        monte_carlo_integral(experiment, number)






