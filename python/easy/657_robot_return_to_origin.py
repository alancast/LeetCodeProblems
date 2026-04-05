class Solution:
    # Just keep track of horizontal and vertical
    # Time O(n)
    # Space O(1)
    def judgeCircle(self, moves: str) -> bool:
        horizontal = vertical = 0

        for char in moves:
            if char == "U":
                vertical += 1
            elif char == "D":
                vertical -= 1
            elif char == "L":
                horizontal -= 1
            elif char == "R":
                horizontal += 1

        return vertical == 0 and horizontal == 0

test_cases = [
    [True, "UD"],
    [False, "LL"]
]
solution = Solution()
for expected, moves in test_cases:
    actual = solution.judgeCircle(moves)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: moves: {moves}")

print("Ran all tests")
