from typing import List


class Solution:
    MOD = pow(10, 9) + 7  # mod defined by problem
    MAX_N = 10010  # Max n defined by problem
    MAX_P = 15  # There are up to 15 prime factors

    # How many ways are there to choose k items from n items (e.g c[n][k])
    c: List[List[int]] = None
    # Array of smallest prime factor for a number (index)
    sieve: List[int]
    # List of prime factors of number (index)
    ps: List[List[int]]
    # How many prime factors of a number (index)
    psLen: List[int]

    def __init__(self):
        Solution.init()

    @staticmethod
    def init():
        # Make sure this only runs once
        if Solution.c is not None:
            return

        Solution.c = [[0] * (Solution.MAX_P + 1) for _ in range(Solution.MAX_N + Solution.MAX_P + 1)]
        Solution.sieve = [0] * Solution.MAX_N
        Solution.ps = [[0] * Solution.MAX_P for _ in range(Solution.MAX_N)]
        Solution.psLen = [0] * Solution.MAX_N

        # Set the smallest prime factor for every number
        for i in range(2, Solution.MAX_N):
            if Solution.sieve[i] == 0:
                for j in range(i, Solution.MAX_N, i):
                    if Solution.sieve[j] == 0:
                        Solution.sieve[j] = i

        for i in range(2, Solution.MAX_N):
            x = i
            while x > 1:
                p = Solution.sieve[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                Solution.ps[i][Solution.psLen[i]] = cnt
                Solution.psLen[i] += 1

        Solution.c[0][0] = 1
        for i in range(1, Solution.MAX_N + Solution.MAX_P + 1):
            Solution.c[i][0] = 1
            for j in range(1, min(Solution.MAX_P, i) + 1):
                Solution.c[i][j] = (Solution.c[i - 1][j] + Solution.c[i - 1][j - 1]) % Solution.MOD

    def idealArrays(self, n: int, maxValue: int) -> int:
        # Go over each ending value
        # See how many ideal arrays there are that end with that ending value
        # Sum them all up
        ans = 0
        for x in range(1, maxValue + 1):
            # Go through each prime factor
            mul = 1
            for p in self.ps[x]:
                mul = mul * self.c[n + p - 1][p] % self.MOD
    
            ans = (ans + mul) % self.MOD

        return ans


test_cases = [
    [10, 2, 5],  # Example: Expected result, n, maxValue
    [11, 5, 3]
]

solution = Solution()
for expected, n, maxValue in test_cases:
    actual = solution.idealArrays(n, maxValue)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, maxValue: {maxValue}")

print("Ran all tests")