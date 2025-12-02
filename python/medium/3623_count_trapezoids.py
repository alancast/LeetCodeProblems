from collections import defaultdict
from typing import List


class Solution:
    MOD = 10**9 + 7

    # Keep track of how many points are at each x
    # Then find total combinations
    # Time O(n)
    # Space O(n)
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # How may points at each y value
        y_count = defaultdict(int)
        for _, y in points:
            y_count[y] += 1
        
        # Go over all y values and add for how many possible edges that value can have
        answer = total_edge_sum = 0
        for count in y_count.values():
            edges = count * (count - 1) // 2
            # Add these edges * running total so far to the answer
            answer = (answer + (edges * total_edge_sum)) % self.MOD
            # Add the new edges to the total
            total_edge_sum = (total_edge_sum + edges) % self.MOD

        return answer

test_cases = [
    [3, [[1,0],[2,0],[3,0],[2,2],[3,2]]],
    [1, [[0,0],[1,0],[0,1],[2,1]]]
]
solution = Solution()
for expected, points in test_cases:
    actual = solution.countTrapezoids(points)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: points: {points}")

print("Ran all tests")