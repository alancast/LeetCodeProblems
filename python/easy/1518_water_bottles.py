class Solution:
    # Time O(n)
    # Space O(1)
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            # Consume numExchange full bottles.
            consumed_bottles += numExchange
            numBottles -= numExchange

            # Exchange them for one full bottle.
            numBottles += 1

        # Consume the remaining numBottles (less than numExchange).
        return consumed_bottles + numBottles

test_cases = [
    [13, 9, 3],
    [19, 15, 4]
]
solution = Solution()
for expected, num_bottles, num_exchange in test_cases:
    actual = solution.numWaterBottles(num_bottles, num_exchange)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num_bottles: {num_bottles}, num_exchange: {num_exchange}")

print("Ran all tests")