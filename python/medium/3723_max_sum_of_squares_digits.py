class Solution:
    # Greedy approach: fill the number with as many 9's as possible, then the remainder, then 0's.
    # Time O(num)
    # Space O(1)
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        # Add 9s then remainder
        q, r = divmod(sum, 9)
        answer = "9" * q
        if r > 0:
            answer += str(r)

        # Fill with 0s to make it num digits long
        answer += "0" * (num - len(answer))

        return answer

test_cases = [
    ["30", 2, 3],
    ["98", 2, 17],
    ["", 1, 10]
]
solution = Solution()
for expected, num, sum in test_cases:
    actual = solution.maxSumOfSquares(num, sum)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: num: {num}, sum: {sum}")

print("Ran all tests")
