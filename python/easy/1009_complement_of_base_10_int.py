class Solution:
    # Check & 1 and shrink num each time
    # Time O(logn)
    # Space O(1)
    def bitwiseComplement(self, n: int) -> int:
        # Corner case
        if n == 0:
            return 1

        answer = 0
        num = 1
        while n > 0:
            if not n & 1:
                answer += num

            num *= 2
            n //= 2

        return answer

test_cases = [
    [2, 5],
    [0, 7],
    [5, 10]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.bitwiseComplement(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
