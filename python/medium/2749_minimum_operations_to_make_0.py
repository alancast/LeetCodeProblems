class Solution:
    # Confusing math, poorly explained
    # Time O(log(num1))
    # Space O(1)
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1

test_cases = [
    [3, 3, -2],
    [-1, 5, 7]
]
solution = Solution()
for expected, num1, num2 in test_cases:
    actual = solution.makeTheIntegerZero(num1, num2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num1: {num1}, num2: {num2}")

print("Ran all tests")