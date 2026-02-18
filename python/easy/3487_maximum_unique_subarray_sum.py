class Solution:
    # Time O(n) as we go over full array once
    # Space O(n) as array could be fully unique
    def maxSum(self, nums: list[int]) -> int:
        total = 0
        max_min = float('-inf')
        nums_set = set()

        for num in nums:
            if num in nums_set:
                continue

            # If all nums in set are neg we want the highest one
            if num < 1:
                max_min = max(max_min, num)
                continue

            nums_set.add(num)
            total += num

        # Had no positive numbers so return least negative
        if total == 0:
            return int(max_min)

        return total

test_cases = [
    [15, [1,2,3,4,5]],
    [1, [1,1,0,1,1]],
    [-1, [-1, -10]],
    [3, [1,2,-1,-2,1,0,-1]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maxSum(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
