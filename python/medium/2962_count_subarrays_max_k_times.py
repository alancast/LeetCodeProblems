from typing import List


class Solution:
    # Keep track of indexes of max num 
    # when we have k compute subarrays that can end at index
    # Time O(n) as only go through nums once
    # Space O(n) worst case every index is max
    def countSubarrays_time_efficient(self, nums: List[int], k: int) -> int:
        max_indexes = []
        n = len(nums)
        count = max = 0

        for end in range(n):
            num = nums[end]

            # See if we have a new max:
            if num > max:
                max = num
                count = 0
                max_indexes.clear()
            
            if num == max:
                max_indexes.append(end)

            if len(max_indexes) >= k:
                count += max_indexes[-k] + 1

        return count

    # Go through nums three times (once for max, once for end and once for start)
    # Time O(n) as each operation through nums is O(1)
    # Space O(1) as we only store ints
    def countSubarrays_memory_efficient(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1

            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1

            count += start

        return count

    # Keep track of indexes of max num 
    # when we have k compute subarrays that can end at index
    # Time O(n) as only go through nums once
    # Space O(k) as we have array of k indexes
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_indexes = []
        n = len(nums)
        count = max = 0

        for end in range(n):
            num = nums[end]

            # See if we have a new max:
            if num > max:
                max = num
                count = 0
                max_indexes.clear()
            
            if num == max:
                max_indexes.append(end)
                if len(max_indexes) > k:
                    max_indexes.pop(0)

            if len(max_indexes) == k:
                count += max_indexes[0] + 1

        return count
    
test_cases = [
    [6, [1,3,2,3,3], 2],
    [5, [1,2,3,4,5], 1],
    [14, [1,1,5,2,5,3,4,5], 2],
    [3, [3,2,1], 1],
    [0, [1,4,2,1], 3]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.countSubarrays_time_efficient(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")