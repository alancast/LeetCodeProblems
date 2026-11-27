from math import sqrt


class Solution:
    # Could be done with just math
    # Time O(1)
    # Space O(1)
    def canAliceWin(self, n: int) -> bool:
        k = int((21 - sqrt(441 - 8 * n)) / 2)
        return k % 2 == 1

    # Each turn removes one fewer stone than the previous turn
    # Simulate until someone cannot make the required move
    # Time O(sqrt(n))
    # Space O(1)
    def canAliceWin_non_math(self, n: int) -> bool:
        stones_to_remove = 10
        alice_turn = True

        # Stop when the player whose turn it is cannot remove enough stones
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn

        # Alice wins if the first player who cannot move is Bob
        return not alice_turn

test_cases = [
    [True, 12],
    [False, 1],
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.canAliceWin(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}")

print("Ran all tests")
