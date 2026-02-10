class Solution:
    # Optimized version of below, where you stop searching if you know can't win
    # Time O(n^2)
    # Space O(n)
    def longestBalanced(self, nums: list[int]) -> int:
        best = 0
        balance = (set(), set())

        # We pop end of nums each time so it slowly shrinks
        while len(nums) > best:
            # Reset sets to start fresh for next search
            balance[0].clear()
            balance[1].clear()

            # Go backwards to start and check each time if balanced
            for idx, num in enumerate(reversed(nums), start=1):
                # Add to either even or odd set
                balance[num & 1].add(num)

                # See if this is balanced
                if len(balance[0]) == len(balance[1]):
                    best = max(best, idx)

            # Pop final num and try again
            nums.pop()

        # Return the longest balanced subarray
        return best

    # Brute force over all start and end points to find longest
    # Keep set of nums seen so far for each one
    # Time O(n^2)
    # Space O(n)
    def longestBalanced_brute(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0

        # Pick starting point
        for i in range(n):
            odds = set()
            evens = set()

            # Pick ending point
            for j in range(i, n):
                if nums[j] & 1:
                    odds.add(nums[j])
                else:
                    evens.add(nums[j])

                if len(odds) == len(evens):
                    answer = max(answer, j - i + 1)

        return answer

test_cases = [
    [4, [2,5,4,3]],
    [5, [3,2,2,5,4]],
    [3, [1,2,3,2]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.longestBalanced(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
