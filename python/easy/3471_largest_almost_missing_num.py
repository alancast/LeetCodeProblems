from collections import defaultdict


class Solution:
    # If k is larger than 1 then only first and last are possible
    # If k is 1 then it's just largest number that appears once
    # One pass, store set and counter
    # Time O(n)
    # Space O(n)
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_num = 0

        # Create counts
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            max_num = max(num, max_num)

        # If n and k are equal return max_num
        if k == n:
            return max_num

        # Only first and last are possible options
        if k > 1:
            if counts[nums[0]] == 1 and counts[nums[-1]] == 1:
                return max(nums[0], nums[-1])
            if counts[nums[0]] == 1:
                return nums[0]
            if counts[nums[-1]] == 1:
                return nums[-1]

            # First and last show up more than once so no num
            return -1

        # When k is 1 just get biggest number that appears once
        answer = -1
        for number, count in counts.items():
            if count == 1:
                answer = max(answer, number)

        return answer

test_cases = [
    [7, [3,9,2,1,7], 3],
    [3, [3,9,7,2,1,7], 4],
    [0, [0,0], 2],
    [8, [11,0,11,0,0,3,3,8], 4],
    [-1, [0,0], 1]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.largestInteger(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
