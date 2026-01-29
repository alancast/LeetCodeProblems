from typing import List


class Solution:
    # Djikstra for each char at a time or Floyd-Warshall
    # Floyd Warshall computes shortest path from i to j
    # So compute all those up front and then just use that for conversion
    # Time O(m + n) m is source length, n is length of original array
    # Space O(1) really O(26x26) but constant so (1)
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Initialize result to store the total minimum cost
        total_cost = 0

        # Minimum transformation cost between any two characters
        min_cost = [[float("inf")] * 26 for _ in range(26)]

        # Fill the initial transformation costs from
        for orig_char, change_char, change_cost in zip(original, changed, cost):
            # Compute start and end index of chars
            start_char_idx = ord(orig_char) - ord("a")
            end_char_idx = ord(change_char) - ord("a")

            # Update cost array
            min_cost[start_char_idx][end_char_idx] = min(
                min_cost[start_char_idx][end_char_idx], change_cost
            )

        # Use Floyd-Warshall algo for shortest path between any two characters
        # Go over all intermediate chars
        for k in range(26):
            # Go over all char combos
            for i in range(26):
                if k == i:
                    continue

                for j in range(26):
                    if k == j or i == j:
                        continue

                    min_cost[i][j] = min(
                        min_cost[i][j], min_cost[i][k] + min_cost[k][j]
                    )

        # Calculate cost to transform string
        for src, tgt in zip(source, target):
            if src == tgt:
                continue

            source_char_idx = ord(src) - ord("a")
            target_char_idx = ord(tgt) - ord("a")

            # If the transformation is not possible, return -1
            if min_cost[source_char_idx][target_char_idx] == float("inf"):
                return -1

            total_cost += min_cost[source_char_idx][target_char_idx]

        return int(total_cost)

test_cases = [
    [28, "abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]],
    [12, "aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]],
    [-1, "abcd", "abce", ["a"], ["e"], [10000]]
]
solution = Solution()
for expected, source, target, original, changed, cost in test_cases:
    actual = solution.minimumCost(source, target, original, changed, cost)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: source: {source}, target: {target}, original: {original}")
        print(f"\tINPUTS: changed: {changed}, cost: {cost}")

print("Ran all tests")
