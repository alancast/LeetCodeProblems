class Solution:
    # Go over moves once and count for all L or all R
    # Time O(n)
    # Space O(1)
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # One line version could be this
        # return abs(moves.count("R") - moves.count("L")) + moves.count("_")

        # Longer easier to read
        all_l = all_r = 0

        # Right is + 1 left is -1
        for char in moves:
            if char == "L":
                all_l -= 1
                all_r -= 1
            elif char == "R":
                all_l += 1
                all_r += 1
            # Try each going all L or all R
            else:
                all_l -= 1
                all_r += 1

        # If we wanted all time max then set answer here within each loop iteration.
        # But I guess question only wants max at end.
        return max(abs(all_l), abs(all_r))

test_cases = [
    [3, "L_RL__R"],
    [5, "_R__LL_"],
    [7, "_______"]
]
solution = Solution()
for expected, moves in test_cases:
    actual = solution.furthestDistanceFromOrigin(moves)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: moves: {moves}")

print("Ran all tests")
