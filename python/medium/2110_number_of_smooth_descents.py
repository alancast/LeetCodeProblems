from typing import List


class Solution:
    # Go over list once and keep track of descent lengths
    # Time O(n)
    # Space O(1)
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        prev_price = prices[0]
        streak_len = 1
        answer = 1

        # Go over all numbers and see if is continuation or not
        for i in range(1,n):
            price = prices[i]
            # Is continuation
            if price == prev_price - 1:
                streak_len += 1
            # New streak starting
            else:
                streak_len = 1

            prev_price = price
            answer += streak_len

        return answer

test_cases = [
    [7, [3,2,1,4]],
    [4, [8,6,7,7]]
]
solution = Solution()
for expected, prices in test_cases:
    actual = solution.getDescentPeriods(prices)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: prices: {prices}")

print("Ran all tests")