from collections import defaultdict


class Solution:
    # Keep a map of used numbers
    # Map values are either 'A', 'B', or 'USED'
    # Go over lists and keep count
    # Time O(n)
    # Space O(n)
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        answer = [0] * n
        common_nums = 0

        # Keep dictionary of what nums we've seen so far
        # Dict instead of set so we don't double count
        used_nums = defaultdict(str)
        USED_STR = 'USED'
        # Go over arrays and see if there is common
        for i in range(n):
            num_a = A[i]
            num_b = B[i]

            # See if the nums create a new shared one
            if used_nums[num_a] == 'B':
                used_nums[num_a] = USED_STR
                common_nums += 1
            else:
                used_nums[num_a] = 'A'

            if used_nums[num_b] == 'A':
                used_nums[num_b] = USED_STR
                common_nums += 1
            else:
                used_nums[num_b] = 'B'

            # Update prefix num
            answer[i] = common_nums

        return answer

test_cases = [
    [[0,2,3,4], [1,3,2,4], [3,1,2,4]],
    [[0,1,3], [2,3,1], [3,1,2]]
]
solution = Solution()
for expected, a, b in test_cases:
    actual = solution.findThePrefixCommonArray(a, b)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: a: {a}, b: {b}")

print("Ran all tests")
