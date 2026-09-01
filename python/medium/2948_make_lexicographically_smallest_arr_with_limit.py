from collections import deque


class Solution:
    # Sort the array and then group into groups all within limit
    # Keep dictionaries of sorted numbers for each group then rebuild answer
    # Time O(nlogn)
    # Space O(n)
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        nums_sorted = sorted(nums)

        curr_group = 0

        # Dictionary of a number to what group it's in
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group

        # Dictionary of a group to all the numbers in that group (sorted)
        group_to_list = {}
        # Use a deque so you can pop left when building answer
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            # If this number is too far away from previous one, start a new group
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1

            # Assign current element to group
            num_to_group[nums_sorted[i]] = curr_group

            # Add element to sorted group deque (make sure group exists first)
            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        # Iterate through input and overwrite each element with the smallest element left in it's group
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            # This makes sure it stays sorted
            nums[i] = group_to_list[group].popleft()

        return nums

test_cases = [
    [[1,3,5,8,9], [1,5,3,9,8], 3],
    [[1,6,7,18,1,2], [1,7,6,18,2,1], 3],
    [[1,7,28,19,10], [1,7,28,19,10], 3],
]
solution = Solution()
for expected, nums, limit in test_cases:
    actual = solution.lexicographicallySmallestArray(nums, limit)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, limit: {limit}")

print("Ran all tests")