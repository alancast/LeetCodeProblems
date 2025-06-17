from typing import List


class Solution:
    MOD = 10**9 + 7

    # This is purely math. It's a really shitty problem tbh
    # Time O(log(n-k))
    # Space O(1)
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        factorial, inverseFactorial = self.computeFactorials(n)
        choosePositions = self.combination(n - 1, k, factorial, inverseFactorial)
        differentChoices = pow(m - 1, n - 1 - k, self.MOD)

        return m * choosePositions % self.MOD * differentChoices % self.MOD
    

    def modularInverse(self, x: int) -> int:
        return pow(x, self.MOD - 2, self.MOD)

    def computeFactorials(self, limit: int) -> int:
        factorial = [1] * (limit + 1)
        inverseFactorial = [1] * (limit + 1)

        for i in range(1, limit + 1):
            factorial[i] = factorial[i - 1] * i % self.MOD

        inverseFactorial[limit] = self.modularInverse(factorial[limit])
        for i in range(limit - 1, -1, -1):
            inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % self.MOD

        return factorial, inverseFactorial

    def combination(self, n: int, k: int, factorial: List[int], inverseFactorial: List[int]) -> int:
        if k < 0 or k > n:
            return 0
    
        return factorial[n] * inverseFactorial[k] % self.MOD * inverseFactorial[n - k] % self.MOD

test_cases = [
    [4, 3, 2, 1],
    [6, 4, 2, 2],
    [2, 5, 2, 0]
]
solution = Solution()
for expected, n, m, k in test_cases:
    actual = solution.countGoodArrays(n, m, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, m: {m}, k: {k}")

print("Ran all tests")