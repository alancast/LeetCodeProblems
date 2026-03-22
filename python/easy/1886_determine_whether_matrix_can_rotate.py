class Solution:
    # Just simulate all 4 rotations
    # Time O(n^2)
    # Space O(1)
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)

        # Just try all 4 rotations
        for _ in range(4):
            # Rotate full matrix clockwise
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    (
                        mat[i][j],
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                    ) = (
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                        mat[i][j],
                    )

            if mat == target:
                return True

        # Went through all 4 and none of them worked, so it's not possible
        return False

test_cases = [
    [True, [[0,1],[1,0]], [[1,0],[0,1]]],
    [False, [[0,1],[1,1]], [[1,0],[0,1]]],
    [True, [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]]
]
solution = Solution()
for expected, mat, target in test_cases:
    actual = solution.findRotation(mat, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: mat: {mat}, target: {target}")

print("Ran all tests")
