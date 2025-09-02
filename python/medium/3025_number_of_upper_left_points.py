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

    # Really dumb just brute forcing it solution
    # Time O(n^3)
    # Space O(1)
    def numberOfPairs_brute_force(self, points: List[List[int]]) -> int:
        n = len(points)

        answer = 0
        # Enumerate all point A's (upper left)
        for i in range(n):
            pointA = points[i]
            # Enumerate all point B's (lower right)
            for j in range(n):
                pointB = points[j]
                # If it's the same point or A is not upper left of B skip this pair
                if i == j or not (
                    pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
                ):
                    continue

                # If there are only 2 points and we get here it means
                # We have an upper left, and only 1 can exist (cuz 2 points)
                # So just return 1 and get out of here
                if n == 2:
                    return 1

                # Make sure all other points aren't in this rectangle
                illegal = False
                for k in range(n):
                    # If this point is one of the others skip
                    if k == i or k == j:
                        continue

                    # See if this point is inside the rectangle of A -> B
                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    )
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    )

                    # If it is inside the rectangle, this A,B pair doesn't count
                    # And break this loop as no other points need checked
                    if isXContained and isYContained:
                        illegal = True
                        break

                # If this pair passed all point K's we have another one for the answer
                if not illegal:
                    answer += 1

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