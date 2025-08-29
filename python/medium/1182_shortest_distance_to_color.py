from collections import defaultdict
from typing import List
from bisect import bisect_left


class Solution:
    # Create map of color nums to list of indexes (O(n))
    # Do binary search on each query and find closest index
    # Time O(n +mlogn) n for creating map, logn for each m queries
    # Space O(n) n for storing map
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # Create and fill color to index mapping list
        color_to_index_list_mapping = defaultdict(list)
        for index, color in enumerate(colors):
            color_to_index_list_mapping[color].append(index)
        
        answer = []
        for index, color in queries:
            # If this color doesn't exist
            if color not in color_to_index_list_mapping:
                answer.append(-1)
                continue

            # Get where this index would be placed in relation to indices of that color
            # Then look at neighbors and see how close nearest is
            color_indices = color_to_index_list_mapping[color]
            insertion_index = bisect_left(color_indices, index)

            # Check neighbors to find the closest
            # If it goes at the end just append distance from the last one
            if insertion_index == len(color_indices):
                answer.append(index - color_indices[-1])
            # If it goes at beginning find distance from first one
            elif insertion_index == 0:
                answer.append(color_indices[0] - index)
            else:
                # Distance to right neighbor
                right = color_indices[insertion_index] - index
                # Distance to left neighbor
                left = index - color_indices[insertion_index - 1]
                answer.append(min(left, right))

        return answer

test_cases = [
    [[3,0,3], [1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]],
    [[-1], [1,2], [[0,3]]]
]
solution = Solution()
for expected, colors, queries in test_cases:
    actual = solution.shortestDistanceColor(colors, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: colors: {colors}, queries: {queries}")

print("Ran all tests")