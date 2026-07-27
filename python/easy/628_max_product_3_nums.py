class Solution:
    # Just go over list once and keep track of the 5 nums we need
    # Time O(n)
    # Space O(1)
    def maximumProduct(self, A: list[int]) -> int:
        # Problem input range is -1000 to 1000
        max_one = max_two = max_three = -1001
        min_one = min_two = 1001

        # Find 3 max and 2 min
        for num in A:
            # Store temp values in case we need to shift values down
            temp_one, temp_two, temp_min_one = max_one, max_two, min_one

            max_one = max(max_one, num)
            max_two = max(max_two, min(temp_one, num))
            max_three = max(max_three, min(temp_two, num))

            min_one = min(min_one, num)
            min_two = min(min_two, max(temp_min_one, num))

        # Answer is one of these two
        return max(max_one * max_two * max_three, max_one * min_one * min_two)

test_cases = [
    [6, [1,2,3]],
    [24, [1,2,3,4]],
    [-6, [-1,-2,-3]]
]
solution = Solution()
for expected, a in test_cases:
    actual = solution.maximumProduct(a)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: a: {a}")

print("Ran all tests")
