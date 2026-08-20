class Solution:
    # Append to arr2 from right to left
    # After end reverse arr2
    # Do it all in one array though with pointers
    # Time O(n)
    # Space O(1)
    def resultArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Get started
        arr = [0] * n
        arr[0] = nums[0]
        arr[n - 1] = nums[1]

        # Go over array and update value in array for whichever it should be appended to
        idx, rev_idx = 0, n - 1
        # Start at 2 because first 2 already placed
        for i in range(2, n):
            # If arr1 end is greater than arr2 put into end of arr 1
            if arr[idx] > arr[rev_idx]:
                idx += 1
                arr[idx] = nums[i]
            # Put into "end" of arr2 (it's backwards)
            else:
                rev_idx -= 1
                arr[rev_idx] = nums[i]

        # Reverse arr2 now
        left, right = rev_idx, n - 1
        while left < right:
            # Swap them and move pointers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


test_cases = [
    [[2,3,1], [2,1,3]],
    [[5,3,4,8], [5,4,3,8]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.resultArray(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
