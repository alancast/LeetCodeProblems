from heapq import heappop, heappush
from typing import List


class Solution:
    # Priority queue to keep lowest sum pairs
    # Also an array to see what's been removed and what's next
    # Time O(nlogn)
    # Space O(n)
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Purely to not modify input
        nums_copy = list(nums)
        # Keep track of what indexes have been removed
        removed = [False] * n

        # What is next index for a given index and previous
        next_indices = [0] * n
        prev_indices = [0] * n
        next_indices[0] = 1
        next_indices[n-1] = -1
        prev_indices[0] = -1
        prev_indices[n-1] = n-2
        for i in range(1, n-1):
            next_indices[i] = i + 1
            prev_indices[i] = i - 1

        # Figure out how many in list are currently unsorted
        count_unsorted = 0
        for i in range(n - 1):
            if nums_copy[i] > nums_copy[i + 1]:
                count_unsorted += 1

        # If already sorted we have our answer
        if count_unsorted == 0:
            return 0

        # Create a min heap of pair sums and their indices
        min_heap = []
        for i in range(n - 1):
            heappush(min_heap, (nums_copy[i] + nums_copy[i + 1], i, i + 1))

        operations = 0
        # Go until it's all sorted
        while count_unsorted > 0 and min_heap:
            curr_sum, idx_one, idx_two = heappop(min_heap)

            # Make sure the sum popped from heap is still valid
            if (removed[idx_one] or 
                next_indices[idx_one] != idx_two or 
                nums_copy[idx_one] + nums_copy[idx_two] != curr_sum):
                continue

            # What has been popped from heap is still valid, so do replacement
            operations += 1
            before_one = prev_indices[idx_one]
            after_two = next_indices[idx_two]

            # See if this removes an unsorted pair
            if nums_copy[idx_one] > nums_copy[idx_two]:
                count_unsorted -= 1
            # See if another unsorted pair is removed
            if before_one != -1 and nums_copy[before_one] > nums_copy[idx_one]:
                count_unsorted -= 1
            # See if a third unsorted pair is removed (though guaranteed to be re_added)
            if after_two != -1 and nums_copy[idx_two] > nums_copy[after_two]:
                count_unsorted -= 1

            # Make operation replacement and update metadata
            nums_copy[idx_one] += nums_copy[idx_two]
            removed[idx_two] = True
            next_indices[idx_one] = after_two

            if after_two != -1:
                prev_indices[after_two] = idx_one

            # If there is number before new num do new checks
            if before_one != -1:
                # See if the new num is less than what comes before it
                if nums_copy[before_one] > nums_copy[idx_one]:
                    count_unsorted += 1

                # Add the new pair to the heap
                heappush(min_heap, (nums_copy[before_one] + nums_copy[idx_one], before_one, idx_one))

            # If there is a number after the new num do new checks also
            if after_two != -1:
                # See if new num is greater than what comes after it
                if nums_copy[idx_one] > nums_copy[after_two]:
                    count_unsorted += 1

                # Add the new pair to the heap
                heappush(min_heap, (nums_copy[idx_one] + nums_copy[after_two], idx_one, after_two))

        return operations

    # Will time out with large arrays
    # Go over whole array every time until sorted
    # Can keep a second array next_index which points to next index
    # This would make deletion O(1) but make space O(n)
    # Time O(n^2)
    # Space O(1)
    def minimumPairRemoval_naive(self, nums: List[int]) -> int:
        n = len(nums)
        pairs_removed = 0

        sorted = False
        # Keep doing operation until sorted
        while not sorted:
            sorted = True
            min_sum_index = 0
            min_sum = float('inf')

            # Go over array to find min sum and see if sorted
            for i in range(1, n - pairs_removed):
                if nums[i-1] > nums[i]:
                    sorted = False
                
                if nums[i-1] + nums[i] < min_sum:
                    min_sum_index = i-1
                    min_sum = nums[i-1] + nums[i]
            
            # See if we need to remove a pair and then do it
            if not sorted:
                nums[min_sum_index] = nums[min_sum_index] + nums[min_sum_index + 1]
                nums.pop(min_sum_index + 1)
                pairs_removed += 1

        return pairs_removed

test_cases = [
    [2, [5,2,3,1]],
    [0, [1,2,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumPairRemoval(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
