from typing import List


class Solution:
    # Net change but space efficient
    # Compute net changes of each number and add positive net changes
    # Store lowest positive net change and closest to 0 negative net change
    # If count of positive net changes is odd either subtract lowest pos or add least neg
    # Time O(n) as we just go through all nums once
    # Space O(1)
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        nums_sum = count_increase = 0
        pos_min = float("inf")
        neg_min = float("-inf")

        # Go through all nums and add net change and update counts
        for num in nums:
            nums_sum += num

            net_change = (num^k) - num
            if net_change > 0:
                count_increase += 1
                nums_sum += net_change
                pos_min = min(pos_min, net_change)
            else:
                neg_min = max(neg_min, net_change)

        # If odd number of net changes make even by either adding or subtracting
        if count_increase % 2 == 1:
            nums_sum -= min(pos_min, abs(neg_min))

        return nums_sum
    
    # Compute net changes of each number and add net changes in even pairs
    # Must be even pairs due to the math theory the whole problem hinges on
    # Time O(nlogn) as we sort net changes which is nlogn
    # Space O(n)
    def maximumValueSum_net_changes_sort(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        # Go through nums and add net changes and compute starting sum
        net_changes = []
        nums_sum = 0
        for num in nums:
            nums_sum += num
            net_change = (num ^ k) - num
            net_changes.append(net_change)

        # Sort net changes in decreasing order
        net_changes.sort(reverse=True)
        
        # Go through the net_changes and add any positive numbers two at a time
        max_sum = nums_sum
        for i in range(0, n-1, 2):
            first_num = net_changes[i]
            second_num = net_changes[i+1]

            net_change = first_num + second_num
            # If net change is below 0 then all future ones will be as well, so exit
            if net_change < 0:
                break

            max_sum += net_change

        return max_sum
    
    # Bottom up DP
    # Time O(n)
    # Space O(n)
    def maximumValueSum_bottom_up_dp(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        # DP[index][isEven] = max of if we do operation on nums before or not
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = -float('inf')
        
        # Go from end to start over all nums
        # Store the sum of if we perform xor on this item or not with the previous max
        for index in range(n - 1, -1, -1):
            for isEven in range(2):
                # Case 1: we perform an operation on this element.
                performOperation = dp[index + 1][isEven ^ 1] + (nums[index] ^ k)
                # Case 2: we don't perform operation on this element.
                dontPerformOperation = dp[index + 1][isEven] + nums[index]

                dp[index][isEven] = max(performOperation, dontPerformOperation)
        
        # Got back to start, return the isEven version as that's an even number of xors
        return dp[0][1]

    # Top down memoization
    # Time O(n) as we go through each num once
    # Space O(n) as we store a memo array of length n
    def maximumValueSum_top_down_dp(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)
    
        # Find max sum of nodes by deciding if value is maxed via xor or not
    # Start with first num and once we get to the end return the max value
    def maxSumOfNodes(self, index: int, isEven: int, nums: List[int], k: int, memo: List[List[int]]) -> int:
        # Final num, if xored an odd number of times can't trust value so return -inf else 0
        if index == len(nums):
            # If the operation is performed on an odd number of elements return INT_MIN
            return 0 if isEven == 1 else -float("inf")
        
        # If we've already computed this just return it
        if memo[index][isEven] != -1:
            return memo[index][isEven]

        # No operation performed on the element
        noXorDone = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        # XOR operation is performed on the element
        xorDone = (nums[index] ^ k) + self.maxSumOfNodes(index + 1, isEven ^ 1, nums, k, memo)

        # Memoize and return whatever result is greater
        memo[index][isEven] = max(xorDone, noXorDone)

        return memo[index][isEven]
    
test_cases = [
    [6, [1,2,1], 3, [[0,1],[0,2]]],
    [9, [2,3], 7, [[0,1]]],
    [42, [7,7,7,7,7,7], 3, [[0,1],[0,2],[0,3],[0,4],[0,5]]]
]
solution = Solution()
for expected, nums, k, edges in test_cases:
    actual = solution.maximumValueSum(nums, k, edges)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}, edges: {edges}")

print("Ran all tests")