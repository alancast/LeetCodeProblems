class Solution:
    # This mod stuff is so stupid. But whatever, part of the problem
    MOD = 10**9 + 7

    # Keep dp array of how many people learned about a secret that day
    # Sum up the newly learned people at end for answer
    # Time O(n)
    # Space O(n)
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # How many people newly learned the secret on day i
        new_learners = [0] * (n + 1)
        # Initial person learns on day 1
        new_learners[1] = 1

        # Go from day 2 until end and see how many people are
        # shared the secret with that day
        share = 0
        for t in range(2, n + 1):
            # New people now able to share after delay
            if t - delay > 0:
                share = (share + new_learners[t - delay] + self.MOD) % self.MOD
            # People no longer sharing because they forgot
            if t - forget > 0:
                share = (share - new_learners[t - forget] + self.MOD) % self.MOD

            new_learners[t] = share

        # Compute how many people know the secret
        # Go from first day no one who learns about it will forget from until end
        answer = 0
        for i in range(n - forget + 1, n + 1):
            answer = (answer + new_learners[i]) % self.MOD

        return answer

test_cases = [
    [5, 6, 2, 4],
    [6, 4, 1, 3]
]
solution = Solution()
for expected, n, delay, forget in test_cases:
    actual = solution.peopleAwareOfSecret(n, delay, forget)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, delay: {delay}, forget: {forget}")

print("Ran all tests")