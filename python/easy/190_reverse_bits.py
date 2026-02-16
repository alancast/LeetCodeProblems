class Solution:
    # Get just do math
    # Time O(32)
    # Space O(32)
    def reverseBits(self, n: int) -> int:
        answer = 0
        power = 31

        # Do the math
        while n:
            answer += (n & 1) << power
            n = n >> 1
            power -= 1

        return answer

test_cases = [
    [964176192, 43261596],
    [1073741822, 2147483644]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.reverseBits(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
