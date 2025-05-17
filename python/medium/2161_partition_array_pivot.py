from typing import List


class Solution:
    # Time O(n) as we go through array twice
    # Space O(1) as all we have is answer array
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        answer = [pivot] * n

        # Go through and put all the low numbers in place
        low_index = high_index = 0
        for num in nums:
            if num < pivot:
                answer[low_index] = num
                low_index += 1
                high_index += 1
            elif num == pivot:
                high_index += 1

        # go through and put high numbers in place too
        for num in nums:
            if num > pivot:
                answer[high_index] = num
                high_index += 1

        return answer
    
    # Time O(n) as we go through array and then merge
    # Space O(n) as we have arrays that add up to space n
    def pivot_array_merge_lists(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        same = []
        higher = []
        for num in nums:
            if num < pivot:
                lower.append(num)
            elif num == pivot:
                same.append(num)
            else:
                higher.append(num)

        return lower + same + higher
    
test_cases = [
    [[9,5,3,10,10,12,14], [9,12,5,10,14,3,10], 10],
    [[-3,2,4,3], [-3,4,3,2], 2]
]
solution = Solution()
for expected, nums, pivot in test_cases:
    actual = solution.pivotArray(nums, pivot)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, pivot: {pivot}")

print("Ran all tests")