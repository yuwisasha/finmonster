"""
https://github.com/norvig/pytudes/blob/main/ipynb/Euler%27s%20Conjecture.ipynb
Сумма четырёх чисел это сумма двух пар чисел, поэтому ищем:
    pair_1 + pair_2 = e**5, где pair_1 = a**5 + b**5 и pair_2 = c**5 + d**5
"""


import itertools


def euler(m: int) -> tuple:
    powers = [e**5 for e in range(2, m)]
    pairs = {
        sum(pair): pair
        for pair in itertools.combinations_with_replacement(powers, 2)
    }
    for pair1 in pairs:
        for e5 in powers:
            pair2 = e5 - pair1
            if pair2 in pairs:
                return fifthroots(pairs[pair1] + pairs[pair2] + (e5,))


def fifthroots(nums: tuple) -> tuple:
    "Sorted integer fifth roots of a collection of numbers."
    res = tuple(sorted(int((x ** (1 / 5))) for x in nums))
    return res


if __name__ == "__main__":
    print(euler(151))  # (a, b, c, d, e)
