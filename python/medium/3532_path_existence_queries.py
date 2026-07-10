class Solution:
    # Union find basically
    # Time O(n + q)
    # Space O(n)
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Set all to the same starting tag
        tags = [0] * n
        # Go over each num, and if they are outside of max diff then separate from neighbor
        for i in range(1, n):
            broken = 1 if nums[i] - nums[i - 1] > maxDiff else 0
            tags[i] = tags[i - 1] + broken

        # Go over each query and see if the numbers are in the same set
        return [tags[x] == tags[y] for x, y in queries]

test_cases = [
    [[True, False], 2, [1,3], 1, [[0,0],[0,1]]],
    [[False, False, True, True], 4, [2,5,6,8], 2, [[0,1],[0,2],[1,3],[2,3]]]
]
solution = Solution()
for expected, n, nums, max_diff, queries in test_cases:
    actual = solution.pathExistenceQueries(n, nums, max_diff, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, nums: {nums}")
        print(f"\tINPUTS: max_diff: {max_diff}, queries: {queries}")

print("Ran all tests")
