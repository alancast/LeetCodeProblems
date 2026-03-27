class Solution:
    # Just go over each row and check row by row
    # Time O(mn)
    # Space O(1)
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])
        k %= cols

        for row in range(rows):
            for col in range(cols):
                # Just check if it equals what it will go to
                if mat[row][col] != mat[row][(col + k) % cols]:
                    return False

        return True

test_cases = [
    [False, [[1,2,3],[4,5,6],[7,8,9]], 4],
    [True, [[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2],
    [True, [[2,2],[2,2]], 3]
]
solution = Solution()
for expected, mat, k in test_cases:
    actual = solution.areSimilar(mat, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: mat: {mat}, k: {k}")

print("Ran all tests")
