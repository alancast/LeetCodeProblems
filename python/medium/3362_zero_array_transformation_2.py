from heapq import heappop, heappush
from typing import List


class Solution:
    # Sort queries, then go through nums and see how many queries needed to zero out
    # Pick ones with furthest ending point first
    # Time O(qlogq + n qlogq) sort queries and then go through nums and find queries to use
    # Space O(sorting algo space + n + q) n for prefix sum, q for query priority queue
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        # Sort queries by starting index
        queries.sort(key=lambda x: x[0])

        prefix_sums = [0] * (n + 1)
        query_used = [False] * q
        queries_used_count = 0
        prefix_sum = 0

        # Go through every num until it can be zero'd
        for i, num in enumerate(nums):
            prefix_sum += prefix_sums[i]

            # We need to use another query
            if num > prefix_sum:
                # Heap of queries sorted by furthest ending
                query_heap = []

                # Find all queries that can get this num updated
                for query_index in range(q):
                    start, end = queries[query_index]
                    # Ends before this num
                    if end < i:
                        continue

                    # Starts after this num
                    if start > i:
                        break

                    # Query already used
                    if query_used[query_index]:
                        continue

                    heappush(query_heap, (-1*end, query_index))

                # Choose queries to use to get num below
                while num > prefix_sum and query_heap:
                    end, index = heappop(query_heap)
                    end *= -1
                    prefix_sum += 1
                    prefix_sums[end + 1] -= 1
                    query_used[index] = True
                    queries_used_count += 1

                # Went through all the queries that can be used and can't 0 out this num
                if num > prefix_sum:
                    return -1

        return q - queries_used_count
    
test_cases = [
    [1, [2,0,2], [[0,2],[0,2],[1,1]]],
    [2, [1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]],
    [18, [5,4,4,2,4,1,4,3,4,5], [[4,7],[2,8],[3,6],[1,7],[7,7],[0,6],[4,5],[2,9],[7,7],[5,5],[8,8],[1,8],[2,6],[4,9],[3,8],[2,3],[5,9],[0,6],[0,2],[0,0],[0,6],[4,7],[1,5],[4,5],[3,9],[5,9],[1,2],[4,8]]],
    [17, [5,3,4,0,3,2,5,3,4,5], [[1,7],[2,3],[4,5],[1,8],[0,1],[3,8],[8,9],[4,7],[1,7],[0,8],[0,5],[3,8],[6,8],[5,9],[5,9],[1,1],[1,5],[2,3],[4,7],[5,5],[3,7],[0,8],[1,5],[4,6],[0,1],[4,9],[8,9],[6,7]]],
    [-1, [1,2,3,4], [[0,3]]]
]
solution = Solution()
for expected, nums, queries in test_cases:
    actual = solution.maxRemoval(nums, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, queries: {queries}")

print("Ran all tests")