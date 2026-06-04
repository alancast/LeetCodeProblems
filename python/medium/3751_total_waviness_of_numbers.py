from functools import lru_cache


class Solution:
    # DP of digits
    # Time O(10^3*lognum2)
    # Space O(10^2*lognum2)
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Calculate the sum of the volatility values of all numbers from 0 up to num
        def solve(num: int) -> int:
            # If the number is less than 3 digits, the fluctuation value is 0
            if num < 100:  # noqa: PLR2004
                return 0

            s = str(num)
            n = len(s)

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and the fluctuation value under current conditions
                cnt = 0
                waviness = 0
                up = int(s[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (digit == 0)
                    # the previous number is updated to curr
                    newPrev = curr
                    # the current number is updated to digit
                    newCurr = -1 if newLeading else digit
                    subCnt, subSum = dfs(
                        pos + 1,
                        newPrev,
                        newCurr,
                        isLimit and (digit == up),
                        newLeading,
                    )
                    # only calculate the volatility value when there are no leading zeros
                    # when the value is a peak or a trough, update the current fluctuation value
                    if not newLeading and prev >= 0 and curr >= 0 and (
                        (prev < curr and curr > digit) or (prev > curr and curr < digit)
                    ):
                        waviness += subCnt

                    cnt += subCnt
                    waviness += subSum

                return cnt, waviness

            _, totalSum = dfs(0, -1, -1, True, True)
            return totalSum

        return solve(num2) - solve(num1 - 1)

test_cases = [
    [3, 120, 130],
    [3, 198, 202],
    [2, 4848, 4848]
]
solution = Solution()
for expected, num_1, num_2 in test_cases:
    actual = solution.totalWaviness(num_1, num_2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num_1: {num_1}, num_2: {num_2}")

print("Ran all tests")
