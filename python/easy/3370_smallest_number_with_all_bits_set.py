class Solution:
    # Time O(logn)
    # Space O(1)
    def smallestNumber(self, n: int) -> int:
        answer = 1
        pow_2 = 2

        while answer < n:
            answer += pow_2
            pow_2 *= 2

        return answer

test_cases = [
    [7, 5],
    [15, 10],
    [3, 3]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.smallestNumber(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
