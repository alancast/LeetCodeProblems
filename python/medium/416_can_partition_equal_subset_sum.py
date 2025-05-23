from functools import lru_cache
from typing import List


class Solution:
    # Bottom up dp fully space optimized so all we need is 1d array
    # Time O(mn)
    # Space O(m)
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        target = nums_sum//2

        # Create a DP array but all we actually need is one row
        dp = [False] * (target + 1)
        dp[0] = True

        # Do bottom up DP but goes down and right to left
        for num in nums:
            for sum_left in range(target, num - 1, -1):
                dp[sum_left] = dp[sum_left] or dp[sum_left - num]

        return dp[target]
    
    # Same approach as bottom up DP below but space optimized
    # With the knowledge that all that matters is the previous row 
    # Time O(mn)
    # Space O(m)
    def canPartition_bottom_up_memory_optimized(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        target = nums_sum//2

        # Create a DP array but all we actually need is one row
        prev = [False] * (target + 1)
        prev[0] = True

        # Do bottom up DP
        for index in range(1, n + 1):
            current_num = nums[index-1]
            current_row = [False] * (target + 1)
            for sum_left in range(target+1):
                if sum_left - current_num < 0:
                    current_row[sum_left] = prev[sum_left]
                else:
                    current_row[sum_left] = prev[sum_left] or prev[sum_left - current_num]

            prev = current_row

        return prev[target]
    
    # Find sum of array, divide by two, and see if you can build a subset that adds to that
    # Use dynamic programming to figure it out
    # Top down dynamic programming to memoize function calls already made
    # Time O(mn)
    # Space O(mn)
    def canPartition_top_down_dp(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            
            # Subcases to evaluate
            result = dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum)
            
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, target)

    # Find sum of array, divide by two, and see if you can build a subset that adds to that
    # Use dynamic programming to figure it out
    # DP[index][sum] = True or False
    # If sum == 0, it's possible so true. If index == len it's not so false
    # Time O(mn)
    # Space O(mn)
    def canPartition_bottom_up_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        target = nums_sum//2

        # Create DP array
        dp = [[False] * (target + 1) for _ in range(n+1)]
        dp[0][0] = True

        # Do bottom up DP
        for index in range(1, n + 1):
            current_num = nums[index-1]
            for sum_left in range(target+1):
                if sum_left - current_num < 0:
                    dp[index][sum_left] = dp[index-1][sum_left]
                else:
                    dp[index][sum_left] = dp[index-1][sum_left] or dp[index-1][sum_left - current_num]

        return dp[n][target]
    
test_cases = [
    [True, [1,5,11,5]],
    [False, [1,2,3,5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.canPartition(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")