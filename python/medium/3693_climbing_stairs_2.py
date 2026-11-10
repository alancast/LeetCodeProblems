class Solution:
    # DP solution
    # Time O(n)
    # Space O(1)
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # Track the minimum costs to reach the previous three steps.
        three_steps_back = two_steps_back = one_step_back = 0

        # Each step can be reached from one, two, or three steps before it.
        for index in range(n):
            step_cost = min(
                three_steps_back + 9,
                two_steps_back + 4,
                one_step_back + 1,
            ) + costs[index]

            # Shift the tracked costs forward for the next step.
            three_steps_back, two_steps_back, one_step_back = (
                two_steps_back,
                one_step_back,
                step_cost,
            )

        return one_step_back

test_cases = [
    [13, 4, [1, 2, 3, 4]],
    [11, 4, [5, 1, 6, 2]],
    [12, 3, [9, 8, 3]],
]
solution = Solution()
for expected, n, costs in test_cases:
    actual = solution.climbStairs(n, costs)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, costs: {costs}")

print("Ran all tests")
