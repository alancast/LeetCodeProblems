class Solution:
    # Binary search with complicated policies
    # Time O(logn)
    # Space O(1)
    def search(self, nums: list[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        while left <= right:
            # To avoid overflow
            mid = left + (right - left) // 2

            # Case 1: We found the target
            if nums[mid] == target:
                return mid

            # Case 2: Mid's left is sorted
            if nums[mid] >= nums[left]:
                # Target is left of mid (or not in list)
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                # Target is right of mid (or not in list)
                else:
                    left = mid + 1

            # Case 3: Mid's right is sorted
            else:  # noqa: PLR5501
                # Target is right of mid (or not in list)
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                # Target is left of mid (or not in list)
                else:
                    right = mid - 1

        # The target isn't in the list
        return -1

test_cases = [
    [4, [4,5,6,7,0,1,2], 0],
    [-1, [4,5,6,7,0,1,2], 3],
    [-1, [1], 0]
]
solution = Solution()
for expected, nums, target in test_cases:
    actual = solution.search(nums, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, target: {target}")

print("Ran all tests")
