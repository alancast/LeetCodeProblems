class Solution:
    # Sort restrictions and see how tall buildings can get
    # Time O(mlogm) for sort
    # Space O(logm) for sort
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        r = restrictions

        # Add restriction (1, 0)
        r.append([1, 0])
        r.sort()

        # Add restriction (n, n-1)
        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)

        # Pass restrictions from left to right
        for i in range(1, m):
            # min of the restriction or previous restriction + distance
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))

        # Pass restrictions from right to left
        for i in range(m - 2, 0, -1):
            # min of the restriction or previous restriction + distance
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        # Go over restrictions and find max height we can get in between them
        answer = 0
        for i in range(m - 1):
            # Calculate the maximum height of the buildings between r[i][0] and r[i][1]
            # Range + two heights // 2
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            answer = max(answer, best)

        return answer

test_cases = [
    [2, 5, [[2,1],[4,1]]],
    [5, 6, []],
    [5, 10, [[5,3],[2,5],[7,4],[10,3]]]
]
solution = Solution()
for expected, n, restrictions in test_cases:
    actual = solution.maxBuilding(n, restrictions)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, restrictions: {restrictions}")

print("Ran all tests")
