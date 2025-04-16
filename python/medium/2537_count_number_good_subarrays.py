from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        self.validate_input(nums, k)
        return self.count_good_two_pointer(nums, k)
    
    def validate_input(self, nums: List[int], k: int) -> None:
        if k < 1 or k > pow(10,9):
            raise ValueError("k must be between 1 and 10^9")
        if len(nums) < 1 or len(nums) > pow(10,5):
            raise ValueError("nums must have between 1 and 10^5 elements")

    # Keep a pointer to left and right and count pairs in between them
    # Time O(n) as we just go through the array once
    # Space O(n) as stores map copy of array
    def count_good_two_pointer(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = subarray_count = good_pairs = 0
        num_count = defaultdict(int)

        # Go through to end and find all good subarrays
        while right < n:
            num = nums[right]

            # This can't add any pairs so just iterate right and continue the loop
            if num_count[num] == 0:
                num_count[num] = 1
                right += 1
                continue

            # See if this num puts us over the good_pair limit
            good_pairs += num_count[num]
            num_count[num] += 1
            # If we do have enough good pairs then add every subarray from her onward to options
            if good_pairs >= k:
                subarray_count += n - right
            
                # Then start subtracting from the left until we no longer have a good subarray
                while left < right:
                    num_left = nums[left]
                    num_count[num_left] -= 1
                    good_pairs -= num_count[num_left]
                    left += 1

                    # If see if the sub array is still good, if so add til end with new starting point
                    if good_pairs >= k:
                        subarray_count += n - right
                    # If not break out of this loop
                    else:
                        break

            right += 1
            

        return subarray_count

    # Exceeds time limit
    # Time O(n^2) as from every index we work down til we get the number of good pairs
    # Space O(n) as stores map copy of array
    def count_good_n2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = 0

        # Enumerate through all subarray starting points
        for i, num in enumerate(nums):
            nums_count = dict()
            nums_count[num] = 1
            good_pairs = 0

            # Enumerate through all subarray ending points
            for j in range(i+1, n):
                num_j = nums[j]
                # This can't add any new pairs
                if num_j not in nums_count:
                    nums_count[num_j] = 1
                    continue

                # Check if this adds a new pair that puts us to k
                # Add all remaining subarrays and break out of loop
                good_pairs += nums_count[num_j]
                nums_count[num_j] += 1
                if good_pairs >= k:
                    # Every subarray from here til end is good
                    subarray_count += n-j                
                    # We know all things after this are already good subarrays
                    # so no need to analyze them
                    break

            nums_count.clear()

        return subarray_count
    
test_cases = [
    [1, [1,1,1,1,1], 10],
    [0, [1], 1],
    [8, [1,1,2,2,3,3,1], 2],
    [4, [3,1,4,3,2,2,4], 2]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.countGood(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")