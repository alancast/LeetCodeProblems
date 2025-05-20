from typing import List


class Solution:
    # Go through all queries and create prefix sum, then go through all nums
    # Time O(n + q) as we go through all nums and all queries once
    # Space O(n) n for prefix sum array
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # n+1 because we put the addition after end
        prefix_sum = [0] * (n + 1)
        running_sum = 0

        for start, end in queries:
            prefix_sum[start] += 1
            prefix_sum[end+1] -= 1

        for i, num in enumerate(nums):
            running_sum += prefix_sum[i]

            # We can't possibly 0 out this number
            if num > running_sum:
                return False

        return True
    
    # Sort queries by start, then go through all nums and prefix sum
    # Time O(n + qlogq) as we go through all nums but also sort all q
    # Space O(n + sorting algo) n for prefix sum array
    def isZeroArray_sorting_queries(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # n+1 because we put the addition after end
        prefix_sum = [0] * (n + 1)
        running_sum = 0

        queries.sort(key=lambda x: x[0])
        q = len(queries)
        query_index = 0

        for i, num in enumerate(nums):
            running_sum += prefix_sum[i]
            # Num can be zero so carry on
            if num <= running_sum:
                continue

            # Num can't be zero so process queries until it can or return False
            while query_index < q and num > running_sum:
                start, end = queries[query_index]
                query_index += 1

                # We sorted by start, so if we are here it means we need to lower this number
                # If start is after this number it means it can't get lower so we fail
                if start > i:
                    return False
                
                # We no longer care about this query
                if end < i:
                    continue

                # We care about this query because it's in the range
                prefix_sum[start] += 1
                running_sum += 1
                prefix_sum[end + 1] -= 1

            # Processed all the queries and couldn't get low enough
            if query_index == q and num > running_sum:
                return False

        return True
    
test_cases = [
    [True, [1,0,1], [[0,2]]],
    [False, [4,3,2,1], [[1,3],[0,2]]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.isZeroArray(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")