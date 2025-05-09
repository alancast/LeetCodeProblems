from math import comb


class Solution:
    # Very confusing, don't really understand
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        tot = 0

        # Count of each num
        digit_count = [0] * 10
        for char in num:
            digit = int(char)
            digit_count[digit] += 1
            tot += digit
    
        # If sum of digits is odd it's impossible to balance even and odd digits so return 0
        if tot % 2 != 0:
            return 0

        target = tot // 2
        max_odd = (n + 1) // 2
        f = [[0] * (max_odd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        psum = tot_sum = 0
        for i in range(10):
            # Sum of the number of the first i digits
            psum += digit_count[i]
            # Sum of the first i numbers
            tot_sum += i * digit_count[i]
            for odd_cnt in range(min(psum, max_odd), max(0, psum - (n - max_odd)) - 1, -1):
                # The number of bits that need to be filled in even numbered positions
                even_cnt = psum - odd_cnt
                for curr in range(min(tot_sum, target), max(0, tot_sum - target) - 1, -1):
                    res = 0
                    for j in range(max(0, digit_count[i] - even_cnt), min(digit_count[i], odd_cnt) + 1):
                        if i * j > curr:
                            break

                        # The current digit is filled with j positions at odd positions, and digit_count[i] - j positions at even positions
                        ways = (comb(odd_cnt, j) * comb(even_cnt, digit_count[i] - j) % MOD)
                        res = (res + ways * f[curr - i * j][odd_cnt - j] % MOD) % MOD

                    f[curr][odd_cnt] = res % MOD

        return f[target][max_odd]    

test_cases = [
    [2, "123"],
    [1, "112"],
    [0, "12345"]
]
solution = Solution()
for expected, num in test_cases:
    actual = solution.countBalancedPermutations(num)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num: {num}")

print("Ran all tests")