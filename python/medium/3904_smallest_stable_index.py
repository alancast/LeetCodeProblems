class Solution:
    # Also same implementation as 3903
    # Same method as below but find min first so that we can stop as soon as we see a stable
    # Find max from left and min from right. Go over array twice
    # Time O(n)
    # Space O(n)
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Min number to the right of this index (n+1 for loop)
        min_right = [9999999999] * (n+1)
        for i in range(n-1, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])

        # Now go from left to right and find max.
        # As soon as find first stable index we have our answer
        answer = -1
        max_left = -9999999999
        # Go from left to right
        for i in range(n):
            # Find new max
            max_left = max(max_left, nums[i])

            # See if index is stable and below k, if so we know it's min
            if max_left - min_right[i] <= k:
                return i

        return answer

    # Find max from left and min from right. Go over array twice
    # Time O(n)
    # Space O(n)
    def firstStableIndex_unoptimized(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Max number to the left of this index
        max_left = [-9999999999] * n
        for i in range(n):
            max_left[i] = max(max_left[i-1], nums[i])

        # Now go from right to left and find smallest stable index
        answer = -1
        min_right = 999999999999
        # Go from right to left
        for i in range(n-1, -1, -1):
            # Find new min
            min_right = min(min_right, nums[i])

            # See if index is stable and below k
            if max_left[i] - min_right <= k:
                answer = i

        return answer

test_cases = [
    [3, [5,0,1,4], 3],
    [-1, [3,2,1], 1],
    [0, [0], 0]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.firstStableIndex(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
