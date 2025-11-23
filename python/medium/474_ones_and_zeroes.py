from typing import Counter, List


class Solution:
    # Faster way to do what's below
    # Time O(n*m*n)
    # Space O(n*m)
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        # Go over every string
        for str in strs:
            ones = 0
            zeroes = 0
            for ch in str:
                if ch == "0":
                    zeroes += 1
                else:
                    ones += 1

            # Update DP values for every string
            new_dp = {}
            # Go over all current entries in dictionary and add new ones
            for k, v in dp.items():
                prev_zeroes, prev_ones = k
                new_zeroes = prev_zeroes + zeroes
                new_ones = prev_ones + ones

                # If this new string is allowed with this combo
                if new_zeroes <= m and new_ones <= n:
                    # Make sure it's a new max
                    if (new_zeroes, new_ones) not in dp:
                        new_dp[(new_zeroes, new_ones)] = v + 1
                    elif dp[(new_zeroes, new_ones)] < v + 1:
                        new_dp[(new_zeroes, new_ones)] = v + 1
            
            # Update the dp with the new values
            dp.update(new_dp)
        
        # Find the max in all the DP values
        return max(dp.values())

    # 2d DP array where it's how many strings can be included with [i][j]
    # dp[i][j]=max(1+dp[i−zeroes_curr][j−ones_curr],dp[i][j])
    # Time O(n*m*n)
    # Space O(n*m)
    def findMaxForm_slow_dp(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Go over all strings
        for str in strs:
            num_counts = Counter(str)
            zero_count = num_counts["0"]
            one_count = num_counts["1"]
            # Update all zero values
            for zeroes in range(m, zero_count-1, -1):
                # Update all one values
                for ones in range(n, one_count-1, -1):
                    dp[zeroes][ones] = max(1+ dp[zeroes - zero_count][ones - one_count], dp[zeroes][ones])

        return dp[m][n]

test_cases = [
    [3, ["10","01","101","0"], 3, 2],
    [4, ["10","0001","111001","1","0"], 5, 3],
    [2, ["10","0","1"], 1, 1]
]
solution = Solution()
for expected, strs, m, n in test_cases:
    actual = solution.findMaxForm(strs, m, n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: strs: {strs}, m: {m}, n: {n}")

print("Ran all tests")