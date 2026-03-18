class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]: # tricky part
                left += 1
            # the first half is ordered
            if nums[left] <= nums[mid]:
                # target is in the first half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # the second half is ordered
            # target is in the second half
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return False

testCases = [
    [[2,5,6,0,0,1,2], 0, True],
    [[2,5,6,0,0,1,2], 3, False]
]
implementation = Solution()
for nums, target, expected in testCases:
    answer = implementation.search(nums, target)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: nums: {nums} target: {target}")

print("Ran all tests")
