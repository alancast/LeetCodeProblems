class Solution:
    # Math of how many ? are left and sums on each side
    # Time O(n)
    # Space O(n)
    def sumGame(self, num: str) -> bool:
        n = len(num)

        # Determine sum of digits as well as how many q in str
        def get(s: str) -> tuple[int, int]:
            digit_sum = q_count = 0
            for ch in s:
                if ch == "?":
                    q_count += 1
                else:
                    digit_sum += int(ch)

            return digit_sum, q_count

        # Find sum and count of both halves
        sum_half_one, q_count_one = get(num[: n // 2])
        sum_half_two, q_count_two = get(num[n // 2 :])

        # The answer scenarios
        # If odd num of ? Alice always wins
        # Otherwise see if sum diff is within bounds of q count diff
        return (q_count_one + q_count_two) % 2 == 1 or sum_half_one - sum_half_two != (q_count_two - q_count_one) * 9 // 2

test_cases = [
    [False, "5023"],
    [True, "25??"],
    [False, "?3295???"]
]
solution = Solution()
for expected, num in test_cases:
    actual = solution.sumGame(num)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num: {num}")

print("Ran all tests")
