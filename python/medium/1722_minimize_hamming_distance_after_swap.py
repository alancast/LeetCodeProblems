from collections import defaultdict


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    # Find what set x belongs to
    def find(self, x: int) -> int:
        # Go until you find the top parent
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    # Union x with y (and by rule all things already unioned with them)
    def union(self, x: int, y: int) -> None:
        # Find the parents
        x_parent = self.find(x)
        y_parent = self.find(y)

        # Just always make x parent (ignore rank efficiency cuz easier to read)
        self.parents[y_parent] = x_parent


class Solution:
    # Union all allowed swap indexes then go through and see what swaps you can make
    # Time O(n + m*u) where m is allowed swaps length and u is union op time
    # Space O(n)
    def minimumHammingDistance(
        self,
        source: list[int],
        target: list[int],
        allowedSwaps: list[list[int]],
    ) -> int:
        n = len(source)

        # Union all the swappable indexes
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        # Count how many of each number are in all swappable sets of source
        count_in_sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            set_id = uf.find(i)
            count_in_sets[set_id][source[i]] += 1

        answer = 0
        # See how many things in target set can be right
        for i in range(n):
            set_id = uf.find(i)

            # See if the desired number is possible, if not add 1 to hamming
            if count_in_sets[set_id][target[i]] > 0:
                count_in_sets[set_id][target[i]] -= 1
            else:
                answer += 1

        return answer

test_cases = [
    [1, [1,2,3,4], [2,1,4,5], [[0,1],[2,3]]],
    [2, [1,2,3,4], [1,3,2,4], []],
    [0, [5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]]
]
solution = Solution()
for expected, source, target, allowed_swaps in test_cases:
    actual = solution.minimumHammingDistance(source, target, allowed_swaps)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: source: {source}, target: {target}, allowed_swaps: {allowed_swaps}")

print("Ran all tests")
