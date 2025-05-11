from typing import List


class Solution:
    # Iterate through each entry in nums and just go through queries as need be
    # Time O(n + k) as we go through nums once and queries once
    # Space O(n) as we store the difference array
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = len(queries)
        difference_array = [0] * (n+1)
        prefix_sum = query_index = 0

        for i, num in enumerate(nums):
            prefix_sum += difference_array[i]
            # If this num isn't 0'd out yet process queries until it is
            while num - prefix_sum > 0:
                # We've processed all the queries and it's still above 0
                if query_index == k:
                    return -1
                
                # Process next query
                start, end, val = queries[query_index]
                query_index += 1

                # Query is in the past
                if i > end:
                    continue

                # Query is in the future
                if i < start:
                    difference_array[start] += val
                    difference_array[end + 1] -= val
                    continue

                # Query is relevant
                prefix_sum += val
                difference_array[end + 1] -= val

        return query_index

    # Binary search to see what k is possible to get a zero array
    # Time O((n + q)*logn) as we call can form logn times
    # Space O(n)
    def minZeroArray_binarySearch(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)

        # Zero array isn't formed after all queries are processed
        if not self._can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search to find min k that it's possible
        while left <= right:
            middle = left + (right - left) // 2
            if self._can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    # Can you form a zero array by processing the first k queries
    # Time O(k + n)
    # Space O(n)
    def _can_form_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        total_sum = 0
        for num_index in range(n):
            total_sum += difference_array[num_index]
            # If total sum is less than the number it means we can't decrement enough to get to 0
            if total_sum < nums[num_index]:
                return False

        # All could get to 0
        return True
    
test_cases = [
    [2, [2,0,2], [[0,2,1],[0,2,1],[1,1,3]]],
    [-1, [4,3,2,1], [[1,3,2],[0,2,1]]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.minZeroArray(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")