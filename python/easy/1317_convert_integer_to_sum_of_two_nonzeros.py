class Solution:
    # Just trial and error until finding a non-zero
    # Time O(n) as we could go over whole thing (kinda)
    # Space O(1)
    def getNoZeroIntegers(self, n: int) -> list[int]:
        # Go over nums from 1 to half of range (no reason to go above half)
        for first_num in range(1, n//2 + 1):
            second_num = n - first_num
            # Make sure there are no zeros
            if "0" not in str(first_num) + str(second_num):
                return [first_num, second_num]

        # If there is no possible way return empty list
        return []

test_cases = [
    [[1,1], 2],
    [[1, 99], 100],
    [[1,8], 9]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.getNoZeroIntegers(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
