from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        self.validate_input(arr)

        return self.len_longest_fib_subsequence_faster_dp(arr)
    
    def validate_input(self, arr: List[int]) -> None:
        if len(arr) < 3 or len(arr) > 1000:
            raise ValueError("arr must be between 3 and 1000 elements")
    
    # Time O(n^2) 
    # Space O(n^2) as we have an NxN 2D DP array
    def len_longest_fib_subsequence_faster_dp(self, arr: List[int]) -> int:
        n = len(arr)
    
        # 2D dp array that stores the length of the longest string that ends at i, j
        # Initialize to 2 to take into account all pairs can be a starting 2 pairs
        dp = [[2] * n for _ in range(n)]
        longest_subsequence = 0

        # Find all two sum pairs before this that add up to this
        for next in range(2, n):
            target_sum = arr[next]
            start = 0
            end = next - 1

            # Find all two sum pairs before this that add up to this and update array
            while start < end:
                sum = arr[start] + arr[end]

                if sum < target_sum:
                    start += 1
                    continue
                if sum > target_sum:
                    end -= 1
                    continue

                # we found a two sum, so iterate DP array and then change start and end
                # But keep searching as there could be multiple pairs that add up to this
                dp[end][next] = dp[start][end] + 1
                longest_subsequence = max(longest_subsequence, dp[end][next])
                start += 1
                end -= 1                

        if longest_subsequence >= 3:
            return longest_subsequence
        return 0
        
    # Time O(n^2) as we iterate over every i,j pair
    # Space O(n^2) as we have an NxN 2D DP array
    def len_longest_fib_subsequence_dp(self, arr: List[int]) -> int:
        n = len(arr)

        # Initialize hash map of all numbers in arr to their index
        nums = dict()
        for i in range(n):
            nums[arr[i]] = i
    
        # 2D dp array that stores the length of the longest string that ends at i, j
        dp = [[0] * n for _ in range(n)]
        longest_subsequence = 0

        for j in range(n):
            for i in range(j):
                b = arr[j]
                a = arr[i]
                diff = b - a
                if diff in nums and diff < a:
                    prev_idx = nums[diff]
                    dp[i][j] = dp[prev_idx][i] + 1
                else:
                    dp[i][j] = 2
                
                longest_subsequence = max(longest_subsequence, dp[i][j])

        if longest_subsequence > 2:
            return longest_subsequence
        return 0
    
    # Time O(n^2) as we iterate through the whole array for each index
    # Worst case scenario would near n^3 as the while loop could loop through the rest of the array
    # But the optimization at the first for loop in practice kills that
    # Space O(n) as we have a hash map of the full array
    def len_longest_fib_subsequence_brute_force(self, arr: List[int]) -> int:
        # Initialize hash map of all numbers in the arr
        nums = set(arr)
        longest_subsequence = 0
        n = len(arr)

        # Start sequence and see how long it can go
        for i in range(n):
            # Minor optimization if we know we can't beat this length
            if longest_subsequence > (n - i):
                break

            temp_subsequence = 0
            for j in range(i+1, n):
                a = arr[i]
                b = arr[j]
                target = a + b
                temp_subsequence = 2

                # See how long sequence can go
                while target in nums:
                    a = b
                    b = target
                    target = a + b
                    temp_subsequence += 1
                
                longest_subsequence = max(temp_subsequence, longest_subsequence)
        
        if longest_subsequence >= 3:
            return longest_subsequence
        return 0
    
test_cases = [
    [5, [1,2,3,4,5,6,7,8]],
    [9, [1,2,3,5,8,13,21,34,55]],
    [3, [1,3,7,11,12,14,18]]
]
solution = Solution()
for expected, arr in test_cases:
    actual = solution.lenLongestFibSubseq(arr)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: arr: {arr}")

print("Ran all tests")