class Solution:
    # Use a sliding window to find target-sum subarrays and track the shortest earlier one
    # Time O(n) as each pointer moves through the array once
    # Space O(n) to store the shortest subarray length before each index
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        array_length = len(arr)
        min_total_length = array_length + 1
        min_length_before = [array_length] * (array_length + 1)
        window_sum = 0
        left = 0
        for right, num in enumerate(arr):
            window_sum += num

            # Shrink the window until its sum is at most target
            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            # Carry forward the shortest target-sum subarray found so far
            min_length_before[right + 1] = min_length_before[right]
            if window_sum == target:
                window_length = right - left + 1
                min_total_length = min(
                    min_total_length,
                    window_length + min_length_before[left],
                )
                min_length_before[right + 1] = min(
                    min_length_before[right],
                    window_length,
                )

        return -1 if min_total_length == array_length + 1 else min_total_length

test_cases = [
    [2, [3, 2, 2, 4, 3], 3],
    [2, [7, 3, 4, 7], 7],
    [-1, [4, 3, 2, 6, 2, 3, 4], 6],
]
solution = Solution()
for expected, arr, target in test_cases:
    actual = solution.minSumOfLengths(arr, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr: {arr}, target: {target}")

print("Ran all tests")
