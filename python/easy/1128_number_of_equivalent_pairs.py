from collections import defaultdict


class Solution:
    # Create a dictionary of pairs to count and return max count
    # Time O(n) where n is len(dominoes) as we just go through it once
    # Space O(1) as there is a finite set of domino combinations that could be in the set
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        pairs_dict = defaultdict(int)
        pair_count = 0

        for domino in dominoes:
            domino.sort()
            pair_count += pairs_dict[tuple(domino)]
            pairs_dict[tuple(domino)] += 1

        return pair_count

test_cases = [
    [1, [[1,2],[2,1],[3,4],[5,6]]],
    [3, [[1,2],[1,2],[1,1],[1,2],[2,2]]],
    [4, [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]],
    [10, [[1,2],[1,2],[1,2],[1,2],[1,2]]]
]
solution = Solution()
for expected, dominoes in test_cases:
    actual = solution.numEquivDominoPairs(dominoes)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: dominoes: {dominoes}")

print("Ran all tests")
