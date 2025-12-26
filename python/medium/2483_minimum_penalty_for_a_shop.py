class Solution:
    # One pass keep count of Y and N and see min
    # Time O(n)
    # Space O(1)
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # Start with closing at hour 0 and assume the current penalty is 0.
        min_penalty = 0
        curr_penalty = 0
        earliest_hour = 0

        for i in range(n):
            # If customer there keeping it open would lower penalty
            if customers[i] == "Y":
                curr_penalty -= 1
            # Otherwise keeping it open increases penalty
            else:
                curr_penalty += 1

            # Update earliest_hour if a smaller penalty is encountered.
            if curr_penalty < min_penalty:
                # Close it the hour after this
                earliest_hour = i + 1
                min_penalty = curr_penalty

        return earliest_hour

test_cases = [
    [2, "YYNY"],
    [0, "NNNNN"],
    [4, "YYYY"]
]
solution = Solution()
for expected, customers in test_cases:
    actual = solution.bestClosingTime(customers)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: customers: {customers}")

print("Ran all tests")