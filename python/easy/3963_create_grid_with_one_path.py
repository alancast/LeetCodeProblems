class Solution:
    # Time O(mn)
    # Space O(n)
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)
