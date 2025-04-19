from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        self._validate_input(nums, lower, upper)
        return self._count_fair_pairs_two_pointers(nums, lower, upper)
    
    # Time O(nlogn) nlogn to sort array then just n go over it with pointers
    # Space O(n) sorting nums
    def _count_fair_pairs_two_pointers(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        # Total pairs is total pairs sum <= upper - sum < lower
        return self._lower_bound(nums, upper + 1) - self._lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def _lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the next index.
            if sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
    
        return result

    # Time O(nlogn) nlogn to sort array then just n to loop through it
    # Space O(n) sorting nums
    def _count_fair_pairs_nlogn(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left = total_pairs = 0
        right = len(nums) - 1

        while left < right:
            num_left = nums[left]
            num_right = nums[right]
            num_sum = num_left + num_right

            if num_sum < lower:
                left += 1
                continue
            if num_sum > upper:
                right -= 1
                continue

            # now see how many pairs are there with this left
            # Can do this with binary search
            lower_right = left + 1
            temp_right = right
            while lower_right < temp_right:
                mid_point = ((lower_right + temp_right) // 2)
                num_mid = nums[mid_point]
                if num_left + num_mid < lower:
                    lower_right = mid_point + 1
                else:
                    temp_right = mid_point

            total_pairs += right - lower_right + 1

            left += 1

        return total_pairs
    
    # Time limit exceeded
    # Time O(n^2) as nested loop through pairs
    # Space O(1)
    def _count_fair_pairs_n2(self, nums: List[int], lower: int, upper: int) -> int:
        fair_pairs = 0
        n = len(nums)

        for i, num_i in enumerate(nums):
            for j in range(i+1, n):
                num_j = nums[j]
                num_sum = num_i + num_j
                if num_sum >= lower and num_sum <= upper:
                    fair_pairs += 1

        return fair_pairs

    def _validate_input(self, nums: List[int], lower: int, upper: int) -> None:
        if len(nums) < 1 or len(nums) > pow(10,5):
            raise ValueError("nums must have length between 1 and 10^5")
        
test_cases = [
    [6, [0,1,7,4,4,5], 3, 6],
    [2, [1,20,21,22], 22, 26],
    [1, [1,7,9,2,5], 11, 11],
    [0, [1,2,3,4], 9, 10],
    [1, [5,4], 3, 10],
    [1, [1,1], 2, 2]
]
solution = Solution()
for expected, nums, lower, upper in test_cases:
    actual = solution.countFairPairs(nums, lower, upper)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, lower: {lower}, upper: {upper}")

print("Ran all tests")