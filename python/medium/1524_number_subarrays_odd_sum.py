from typing import List
from math import comb

class Solution:
    MOD = pow(10, 9) + 7

    def numOfSubarrays(self, arr: List[int]) -> int:
        self.validate_input(arr)
        return self.num_subarrays_prefix_sums(arr)

    # Time O(n) goes through full array once
    # Space O(1)
    def num_subarrays_prefix_sums(self, arr: List[int]) -> int:
        prefix_sum = count = odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                even_count += 1
                count += odd_count
            else:
                odd_count += 1
                count += even_count

            count %= self.MOD  # To handle large results

        return count
    
    # Time O(n) goes through full array once
    # Space O(1) only maintains a constant 2x2 array
    def num_subarrays_dp(self, arr: List[int]) -> int:
        # dp to track counts for even and odd sum subarrays
        # dp[0][idx] is for sums that are even
        # dp[1][idx] is for sums that are odd
        # We only care about subarray sums from the previous index
        dp = [[0, 0], [0, 0]]

        # Stores the final count of subarrays with an odd sum
        count = dp[1][0]

        for i in range(len(arr)):
            # Alternates between 0 and 1 as we only care about previous index counts
            idx = i & 1
            # Determines if the current element is odd (1) or even (0)
            parity = arr[i] & 1
            
            # If the current element is odd, it contributes to odd subarrays
            # If the current element is even, it contributes to even subarrays
            dp[parity][idx] = (1 + dp[0][1 - idx]) % self.MOD
            dp[1 - parity][idx] = dp[1][1 - idx] % self.MOD
            
            # Accumulate the count of odd subarrays
            count = (count + dp[1][idx]) % self.MOD

        return count
    
    def validate_input(self, arr: List[int]) -> None:
        if len(arr) < 1 or len(arr) > pow(10,5):
            raise ValueError("arr must have between 1 and 10^5 entries in it")
        for num in arr:
            if num < 1 or num > 100:
                raise ValueError("every item in arr must be between 1 100")

    
test_cases = [
    [20, [2,1,2,2,1,2,1,2]],
    [4, [1,1,1]],
    [4, [1,3,5]],
    [6, [1,1,3,5]],
    [0, [2,4,6]],
    [16, [1,2,3,4,5,6,7]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.numOfSubarrays(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")