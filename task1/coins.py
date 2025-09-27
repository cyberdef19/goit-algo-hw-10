from random import randint
import timeit

def find_coins_greedy(sum_coins: int) -> dict:
    banknotes = [50, 25, 10, 5, 2, 1]
    coins = {}

    for banknote in banknotes:
        sc = sum_coins//banknote
        if sc > 0:
            coins[banknote] = sc
            sum_coins -= banknote * sc
        else:
            continue
    return coins


def find_min_coins(amount: int) -> dict:
    coins = [1, 2, 5, 10, 25, 50]

    # dp[i] = мінімальна кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # базовий випадок: 0 монет на суму 0

    # prev[i] = яка монета була останньою для цієї суми
    prev = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    # Відновлюємо набір монет
    result = {}
    curr = amount
    while curr > 0:
        coin = prev[curr]
        result[coin] = result.get(coin, 0) + 1
        curr -= coin

    return result

test_sums = [randint(100, 10000) for _ in range(10)]

for sum_coins in test_sums:

    greedy_time = timeit.timeit(lambda: find_coins_greedy(sum_coins), number=1000)
    gredy_result = find_coins_greedy(sum_coins)
    greedy_count = sum(gredy_result.values())

    min_coins_time = timeit.timeit(lambda: find_min_coins(sum_coins), number=1000)
    min_coins_result = find_min_coins(sum_coins)
    min_coins_count = sum(min_coins_result.values())

    print(f"Сума {sum_coins}")
    print(f"Жадібний: кількість монет:{greedy_count} час виконання {greedy_time}")
    print(f"Динамічний: кількість монет:{min_coins_count} час виконання {min_coins_time}")










