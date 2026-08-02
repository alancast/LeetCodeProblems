from functools import lru_cache


class Solution:
    # Turns out you can show Alice just always wins
    # Time O(1)
    # Space O(1)
    def stoneGame(self, piles: list[int]) -> bool:
        return True

    # Add points for Alice, subtract for Bob
    # At each time just see which one is optimal move
    # Time O(n^2)
    # Space O(n^2)
    def stoneGame_dp(self, piles: list[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            # We have taken all the piles, nothing left to take, game is over
            if i > j:
                return 0

            parity = (j - i - N) % 2
            if parity == 1:
                # Player is Alice so add points
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))

            # Player is Bob so subtract points
            return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0

test_cases = [
    [True, [5,3,4,5]],
    [True, [3,7,2,3]]
]
solution = Solution()
for expected, piles in test_cases:
    actual = solution.stoneGame(piles)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {piles}")

print("Ran all test")
