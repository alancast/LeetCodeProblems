from typing import List


class Solution:
    # Time O(plogp + tlogt)
    # Space O(p + t) for sorting
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        p = len(players)

        trainers.sort()

        matches = player_index = 0

        for trainer in trainers:
            # Make sure we haven't run out of players
            if player_index >= p:
                break

            if trainer >= players[player_index]:
                matches += 1
                player_index += 1

        return matches
    
test_cases = [
    [2, [4,7,9], [8,2,5,8]],
    [1, [1,1,1], [10]]
]
solution = Solution()
for expected, players, trainers in test_cases:
    actual = solution.matchPlayersAndTrainers(players, trainers)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: players: {players}, trainers: {trainers}")

print("Ran all tests")