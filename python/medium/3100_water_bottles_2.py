import math


class Solution:
    # Can be done with math in O(1)
    # Time O(sqrt(n))
    # Space O(1)
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        delta = b * b - 4 * a * c
        t = math.ceil((-b + math.sqrt(delta)) / (2 * a))
        return numBottles + t - 1

    # Time O(sqrt(n))
    # Space O(1)
    def numWaterBottles_simulation(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = numBottles
        empty = numBottles

        while empty >= numExchange:
            consumed_bottles += 1
            empty -= numExchange - 1
            numExchange += 1

        return consumed_bottles

test_cases = [
    [15, 13, 6],
    [13, 10, 3]
]
solution = Solution()
for expected, num_bottles, num_exchange in test_cases:
    actual = solution.numWaterBottles(num_bottles, num_exchange)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num_bottles: {num_bottles}, num_exchange: {num_exchange}")

print("Ran all tests")