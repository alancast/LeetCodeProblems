from typing import List


class Solution:
    # Go over all elements once, do bound checking and simple math of where
    # next entry would be for diagonals with each time
    # Time O(n*m) as we go over everything once with O(1) operations
    # Space O(1) as all that's stored is answer array
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        n = len(mat)
        m = len(mat[0])
        row = column = 0

        # What direction are we processing the current diagonal
        # top right to bottom left (1) or bottom left to top right (0)
        direction = 1

        # Iterate over all the elements in the array and put them into answer
        # This will kick out as soon as we can't get a row or column within bounds
        answer = []
        while row < n and column < m:
            answer.append(mat[row][column])

            # Move along the diagonal depending on direction
            # [i, j] -> [i - 1, j + 1] if going up (direction == 1)
            # [i, j] -> [i + 1][j - 1] if going down (direction == 0)
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)

            # Make sure next element is within bounds
            # If not, find next one which is
            if new_row < 0 or new_row == n or new_column < 0 or new_column == m:
                # Going up, so now go down
                if direction == 1:
                    # With (i,j) as tail, if (i,j+1) is within bounds, it's next head.
                    # Otherwise, the element directly below (i+1,j) is next head
                    row += (1 if column == m - 1 else 0)
                    column += (1 if column < m - 1 else 0)
                # Going down so now go up
                else:
                    # With (i,j) as tail, if (i+1,j) is within bounds, it's next head
                    # Otherwise element directly to the right (i, j+1) is next head
                    column += (1 if row == n - 1 else 0)
                    row += (1 if row < n - 1 else 0)

                # Flip the direction
                direction = 1 - direction
            # Next element was already within bounds so just do the switch
            else:
                row = new_row
                column = new_column

        return answer

test_cases = [
    [[1,2,4,7,5,3,6,8,9], [[1,2,3],[4,5,6],[7,8,9]]],
    [[1,2,3,4], [[1,2],[3,4]]]
]
solution = Solution()
for expected, mat in test_cases:
    actual = solution.findDiagonalOrder(mat)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: mat: {mat}")

print("Ran all tests")