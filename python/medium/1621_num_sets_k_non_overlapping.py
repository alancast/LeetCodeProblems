from math import comb


class Solution:
    # Just a math combinatorics problem
    # Time O(k + logM) (M is the modulus) for the comb function
    # Space O(1)
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, k * 2) % (10**9 + 7)

test_cases = [
    [5, 4, 2],
    [3, 3, 1],
    [796297179, 30 , 7]
]
solution = Solution()
for expected, n, k in test_cases:
    actual = solution.numberOfSets(n, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, k: {k}")

print("Ran all tests")
