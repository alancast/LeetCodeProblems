from collections import defaultdict


class Solution:
    # Preprocess nearest left and right neighbor for each index
    # Time O(n + q)
    # Space O(n)
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)

        # Index of closest same num to left and right
        left = [0] * n
        right = [0] * n
        last_time_seen_num = {}

        # Find nearest left neighbor for each element (go from -n to n for circular)
        for i in range(-n, n):
            # We know last time seen num is fully populated now
            # So start storing closest left neighbor
            if i >= 0:
                left[i] = last_time_seen_num[nums[i]]
            # Keep track of last time we saw this number
            last_time_seen_num[nums[(i + n) % n]] = i

        # Find nearest right neighbor for each element (go from 2n to 0 for circular)
        last_time_seen_num.clear()
        for i in range((2*n)-1, -1, -1):
            # We know last time seen num is fully populated now
            # So start storing closest left neighbor
            if i < n:
                right[i] = last_time_seen_num[nums[i]]
            # Keep track of last time we saw this number
            last_time_seen_num[nums[i % n]] = i

        # Go over all queries and find closest answer
        answer = []
        for index in queries:
            # This means the number appears in there only once
            if index - left[index] == n:
                answer.append(-1)
            # Appears multiple times so find min answer
            else:
                answer.append(min(index - left[index], right[index] - index))

        return answer

    # Too slow
    # Create a hash map of indexes of all elements in num
    # For each query go over indices and find answer
    # Time O(n^2) worst case where all elements in array are same num
    # Space O(n)
    def solveQueries_brute(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)

        # Populate element indices
        element_indices = defaultdict(list)
        for index, num in enumerate(nums):
            element_indices[num].append(index)

        answer = []
        # Go over each query and find min distance
        for index in queries:
            target_num = nums[index]

            min_distance = float('inf')

            # Go over indices for num and find min distance
            for num_index in element_indices[target_num]:
                if num_index == index:
                    continue

                distance = min(abs(index - num_index), index + n - num_index, num_index + n - index)
                min_distance = min(min_distance, distance)

            if min_distance == float('inf'):
                answer.append(-1)
            else:
                answer.append(min_distance)

        return answer

test_cases = [
    [[2,-1,3], [1,3,1,4,1,3,2], [0,3,5]],
    [[-1,-1,-1,-1], [1,2,3,4], [0,1,2,3]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.solveQueries(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")
