class Solution:
    # Keep the longest middle subarray whose sum is total - x
    # Time O(n)
    # Space O(1)
    def minOperations(self, nums: list[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        INF = 9999999999999
        mini = INF
        left = 0

        for right in range(n):
            # Remove nums[right] from the remaining sum
            current -= nums[right]

            # If the remaining sum is too small, add values back from the left
            while current < x and left <= right:
                current += nums[left]
                left += 1

            # If the removed values sum to x, update the minimum operations
            if current == x:
                mini = min(mini, (n-1-right)+left)

        return mini if mini != INF else -1

test_cases = [
    [2, [1,1,4,2,3], 5],
    [-1, [5,6,7,8,9], 4],
    [5, [3,2,20,1,1,3], 10]
]
solution = Solution()
for expected, nums, x in test_cases:
    actual = solution.minOperations(nums, x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, x: {x}")

print("Ran all tests")
