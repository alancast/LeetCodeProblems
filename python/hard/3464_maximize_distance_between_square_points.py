from bisect import bisect_left


class Solution:
    # Unfold square into one dimensional array
    # Then use binary search to pick k points with min manhattan
    # Upper bound is side length because if more than 4 less than side, and if 4 then equal side
    # Time O(nklogn)
    # Space O(n)
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # Flatten points into one dimensional array
        flattened_points = []
        for x, y in points:
            if x == 0:
                flattened_points.append(y)
            elif y == side:
                flattened_points.append(side + x)
            elif x == side:
                flattened_points.append(side * 3 - y)
            else:
                flattened_points.append(side * 4 - x)

        flattened_points.sort()

        # See if it's possible to select k points where each one is at least limit away from all others
        def check(limit: int) -> bool:
            perimeter = side * 4

            # Go over all points
            for start in flattened_points:
                end = start + perimeter - limit
                cur = start

                # Try to find next k points making sure each one is at least limit away
                for _ in range(k - 1):
                    idx = bisect_left(flattened_points, cur + limit)
                    if idx == len(flattened_points) or flattened_points[idx] > end:
                        cur = -1
                        break

                    # Update the last point we got
                    cur = flattened_points[idx]

                # See if it was possible
                if cur >= 0:
                    return True

            # We went over all points and it was not possible
            return False

        # Do binary search to find answer
        low = 1
        high = side
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
                answer = mid
            else:
                high = mid - 1

        return answer

test_cases = [
    [2, 2, [[0,2],[2,0],[2,2],[0,0]], 4],
    [1, 2, [[0,0],[1,2],[2,0],[2,2],[2,1]], 4],
    [1, 2, [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], 5]
]
solution = Solution()
for expected, side, points, k in test_cases:
    actual = solution.maxDistance(side, points, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: side: {side}, points: {points}, k: {k}")

print("Ran all tests")
