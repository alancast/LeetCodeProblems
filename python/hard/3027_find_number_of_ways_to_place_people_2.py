from typing import List


class Solution:
    # Sort points so it goes left and downward
    # Time O(nlogn + n^2)
    # Space O(n) for sorting
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points so it is now going from left to right and top to bottom
        points.sort(key=lambda x: (x[0], -x[1]))

        answer = 0
        # Go over all point A's (upper left) 
        # We don't care about x because it's already sorted left to right
        for i, (_, top) in enumerate(points):
            bottom = float("-inf")

            # Go over all point B's after A in the list
            # We again don't care about x because it's already sorted left to right
            for (_, y) in points[i + 1:]:
                # If this is above previous bottom update bottom and count answer
                # We know any points on line below this won't matter because of sorting
                # Think example [1,9], [1,1], [1,3]
                if bottom < y <= top:
                    answer += 1
                    bottom = y

                    # If top == bottom that means we found a point directly to the right
                    # of point A, so break out of this loop as no points after this can be valid
                    if top == bottom:
                        break

        return answer

test_cases = [
    [0, [[1,1],[2,2],[3,3]]],
    [2, [[6,2],[4,4],[2,6]]],
    [2, [[3,1],[1,3],[1,1]]]
]
solution = Solution()
for expected, points in test_cases:
    actual = solution.numberOfPairs(points)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: points: {points}")

print("Ran all tests")