from collections import defaultdict, Counter
from typing import List

class Solution:
    # Time O(n) Space O(n)
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_counts = []
        ball_to_color_map = defaultdict(int)
        color_counter = Counter()

        for query in queries:
            ball = query[0]
            color = query[1]

            # Make sure the new color is accounted for
            color_counter[color] = color_counter.get(color, 0) + 1

            # See if there is an old color we need to remove
            if ball in ball_to_color_map:
                old_color = ball_to_color_map[ball]
                color_counter[old_color] -= 1
                if color_counter[old_color] == 0:
                    del color_counter[old_color]

            # Make sure new ball color is stored
            ball_to_color_map[ball] = color

            color_counts.append(len(color_counter))

        return color_counts
    
testCases = [
    [4, [[1,4],[2,5],[1,3],[3,4]], [1,2,2,3]],
    [4, [[1,4],[1,5]], [1,1]]
]
solution = Solution()
for limit, queries, expected in testCases:
    answer = solution.queryResults(limit, queries)
    if answer != expected:
        print(f"FAILED TEST! Expected {expected} but got {answer}. INPUTS: limit: {limit}, queries: {queries}")

print("Ran all tests")