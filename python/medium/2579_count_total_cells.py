class Solution:
    # Time O(1) as it's just a math formula
    # Space O(1) as we don't need any new space
    def coloredCells(self, n: int) -> int:
        return 1 + ((2 * n) * (n - 1))
    
    # Time O(n) as we need to compute up to n
    # Space O(1) as we just need to know what last number was
    def coloredCells_iterative(self, n: int) -> int:
        if n == 1:
            return 1
        
        i = 2
        num_cells = 5

        while i < n:
            # Compute next value
            num_cells += (4 * i)
            i += 1

        return num_cells
        

test_cases = [
    [1, 1],
    [5, 2],
    [13, 3],
    [25, 4],
    [41, 5],
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.coloredCells(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")