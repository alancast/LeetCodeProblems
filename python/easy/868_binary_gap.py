class Solution:
    # Just go over binary digits
    # Time O(1)
    # Space O(1)
    def binaryGap(self, n: int) -> int:
        if (n & (n - 1)) == 0:
            return 0
        n //= n & -n

        # Shrink n until through all bits
        answer = 0
        gap = 0
        while n:
            if n & 1:
                answer = max(answer, gap)
                gap = 0
            else:
                gap += 1
            n >>= 1

        return answer + 1

test_cases = [
    [2, 22],
    [0, 8],
    [2, 5]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.binaryGap(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
