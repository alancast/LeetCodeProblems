from typing import List


class Solution:
    # This problem is silly. But the 3 kids each only get n-1 moves
    # So the kid starting at 0,0 must just take the diagonal
    # The kid starting top right and bottom right never cross that diagonal
    # otherwise they can't make it. So just compute maxes for those 2 kids
    # add the diagonal and done.
    # Time O(n^2) as we go over the grid
    # Space O(n)
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # Compute the diagonal path (for kid at 0,0)
        answer = sum(fruits[i][i] for i in range(n))

        # Dynamic programming to find max amount this person can get
        # O(n^2) and space O(n)
        def dp():
            # Start them both at all neg infinity
            # Because we only update if new value is greater than what's there
            prev = [float("-inf")] * n
            curr = [float("-inf")] * n

            # Initialize the value with the fruit at top right (starting point)
            prev[n - 1] = fruits[0][n - 1]

            # Iterate over max of all previous ones and store that in the max of current
            # dp[i][j]=max(dp[i−1][j−1], dp[i−1][j], dp[i−1][j+1])+fruits[i][j].
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])

                    curr[j] = best + fruits[i][j]
                
                # Swap current and previous
                temp = prev
                prev = curr
                curr = temp

            return prev[n - 1]

        # Add the amount for the kid starting top right
        answer += dp()

        # Invert the grid to use the same dp function for the other diagonal
        for i in range(n):
            for j in range(i):
                temp = fruits[i][j]
                fruits[i][j] = fruits[j][i]
                fruits[j][i] = temp

        # Add the amount for the kid starting bottom left
        answer += dp()

        return answer 
   
test_cases = [
    [100, [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]],
    [4, [[1,1],[1,1]]]
]
solution = Solution()
for expected, fruits in test_cases:
    actual = solution.maxCollectedFruits(fruits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: fruits: {fruits}")

print("Ran all tests")