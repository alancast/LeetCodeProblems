from math import inf


class Solution:
    # Time O(n)
    # Space O(1)
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count("0")

        if n == k:
            return 0 if zeros == 0 else 1 if zeros == n else -1

        ans = inf
        if zeros % 2 == 0:
            m = max((zeros + k - 1) // k, (zeros + n - k - 1) // (n - k))
            m += m & 1
            ans = min(ans, m)
        if zeros % 2 == k % 2:
            m = max((zeros + k - 1) // k, (n - zeros + n - k - 1) // (n - k))
            m += m & 1 == 0
            ans = min(ans, m)

        return int(ans) if ans < inf else -1

test_cases = [
    [1, "110", 1],
    [2, "0101", 3],
    [-1, "101", 2]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.minOperations(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")
