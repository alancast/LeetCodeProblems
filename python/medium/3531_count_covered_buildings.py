from typing import List


class Solution:
    # Find max and min buildings in each row and col
    # Then go over all the buildings and see if they are covered
    # Time O(b)
    # Space O(n)
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Initialize data structures to keep min and max row and cols
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        # Go over all buildings and update rows and cols accordingly
        for x, y in buildings:
            max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)

        answer = 0
        # Go over all buildings again and see if covered
        for x, y in buildings:
            # Blocked on both sides on the rows
            row_between = min_row[y] < x < max_row[y]
            # Blocked on both sides of the cols
            col_between = min_col[x] < y < max_col[x]
            if row_between and col_between:
                answer += 1

        return answer

test_cases = [
    [1, 3, [[1,2],[2,2],[3,2],[2,1],[2,3]]],
    [0, 3, [[1,1],[1,2],[2,1],[2,2]]],
    [1, 5, [[1,3],[3,2],[3,3],[3,5],[5,3]]]
]
solution = Solution()
for expected, n, buildings in test_cases:
    actual = solution.countCoveredBuildings(n, buildings)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, buildings: {buildings}")

print("Ran all tests")
