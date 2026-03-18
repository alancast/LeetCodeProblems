class Solution:
    # Bitmasking
    def subsets(self, nums: list[int]) -> list[list[int]]:
        allSubsets = []
        n = len(nums)

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            allSubsets.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return allSubsets

    def subsetsBacktracking(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first = 0, curr = None):
            if curr is None:
                curr = []
            if len(curr) == k:
                allSubsets.append(curr[:])
                return

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        allSubsets = []
        n = len(nums)
        for k in range(n + 1):  # noqa: B007
            backtrack()
        return allSubsets

    def subsetsBrute(self, nums: list[int]) -> list[list[int]]:
        allSubsets = [[]]
        for num in nums:
            previous_subsets = allSubsets.copy()
            for subset in previous_subsets:
                next_subset = subset.copy()
                next_subset.append(num)
                allSubsets.append(next_subset)

        return allSubsets

"""
testCases = [
    [[1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]],
    [[0], [[],[0]]]
]
solution = Solution()
for nums, expected in testCases:
    answer = solution.subsets(nums)
    if answer != expected:
        print(f"FAILED TEST: Expected: {expected}, got {answer}. INPUT {nums}")
"""
