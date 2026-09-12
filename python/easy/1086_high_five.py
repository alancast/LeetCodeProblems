from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    # Map and min heap
    # Time O(nlogk)
    # Space O(n)
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores = defaultdict(list)
        for id, score in items:
            heappush(scores[id], score)
            # Make sure to only take top 5 scores
            while len(scores[id]) > 5:  # noqa: PLR2004
                heappop(scores[id])

        # Return the student scores
        return [[id, sum(scores[id])//len(scores[id])] for id in sorted(scores.keys())]

test_cases = [
    [[[1,87],[2,88]], [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]],
    [[[1,100],[7,100]], [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]]
]
solution = Solution()
for expected, items in test_cases:
    actual = solution.highFive(items)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: items: {items}")

print("Ran all tests")
