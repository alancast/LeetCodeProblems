class Solution:
    # DFS to see what you an go to starting from each one
    # Time O(n*d)
    # Space O(n)
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        seen = {}

        def dfs(pos):
            if pos in seen:
                return
            seen[pos] = 1

            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1
            i = pos + 1
            while i < n and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1

        for i in range(n):
            dfs(i)

        return max(seen.values())

test_cases = [
    [4, [6,4,14,6,8,13,9,7,10,6,12], 2],
    [1, [3,3,3,3,3], 3],
    [7, [7,6,5,4,3,2,1], 1]
]
solution = Solution()
for expected, arr, d in test_cases:
    actual = solution.maxJumps(arr, d)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr: {arr}, d: {d}")

print("Ran all tests")
