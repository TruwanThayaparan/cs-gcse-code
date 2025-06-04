# Challenge 78 - 2 fiddy
def count_ways_to_make(amount_pence, coins):
    ways = [0] * (amount_pence + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amount_pence + 1):
            ways[i] += ways[i - coin]

    return ways[amount_pence]

amount = 250
coins = [200, 100, 50, 20, 10, 5, 2, 1]

total_ways = count_ways_to_make(amount, coins)
print(f"Total ways to make £2.50: {total_ways}")
