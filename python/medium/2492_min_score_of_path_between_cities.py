class Solution:
    # Union find, where you store shortest edge in union
    # Could also just do one BSF
    # Time O(n + e)
    # Space O(n) for queue as well as graph
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # The uf tree where everything starts as it's own root
        root = list(range(n + 1))

        def find(i: int) -> int:
            root[i] = find(root[i]) if root[i] != i else i
            return root[i]

        # Join all unions that are together
        for x, y, _ in roads:
            root[find(x)] = find(y)

        # Just a very large initial answer
        answer = 999999999

        # Go over all roads and find shortest one in this group
        root_1 = find(1)
        for x, _, d in roads:
            if find(x) == root_1:
                answer = min(answer, d)

        return answer

test_cases = [
    [5, 4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]],
    [2, 4, [[1,2,2],[1,3,4],[3,4,7]]]
]
solution = Solution()
for expected, n, roads in test_cases:
    actual = solution.minScore(n, roads)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, roads: {roads}")

print("Ran all tests")
