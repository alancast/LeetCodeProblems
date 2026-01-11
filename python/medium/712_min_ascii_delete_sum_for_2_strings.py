class Solution:
    # Same logic as below but noticed only need previous row
    # So simplify space storage
    # Time O(m*n)
    # Space O(m)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Make sure s2 is always the smaller string
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1 = s2, s2 = s1)

        m = len(s1)
        n = len(s2)

        # Base case of empty s1
        curr_row = [0] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = curr_row[j - 1] + ord(s2[j - 1])
        
        # Compute answer row-by-row
        for i in range(1, m + 1):
            diag = curr_row[0]
            curr_row[0] += ord(s1[i - 1])

            for j in range(1, n + 1):
                # If characters are the same, the answer is top-left-diagonal value
                if s1[i - 1] == s2[j - 1]:
                    answer = diag
                # Otherwise, the answer is minimum of top and left values with
                # deleted character's ASCII value
                else:
                    answer = min(
                        ord(s1[i - 1]) + curr_row[j],
                        ord(s2[j - 1]) + curr_row[j - 1]
                    )

                # Before overwriting curr_row[j] with the answer, save it in diag
                # for the next column
                diag = curr_row[j]
                curr_row[j] = answer
        
        # Return final answer
        return curr_row[-1]

    # Keep DP array of min possible cost to make strings equal
    # Each entry can be determined by
    # min(cost to left + delete up, cost up + delete left)
    # Time O(m*n)
    # Space O(m*n)
    def minimumDeleteSum_not_space_optimized(self, s1: str, s2: str) -> int:
        # Prepare the two-dimensional array
        m = len(s1)
        n = len(s2)
        compute_cost = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the base case values of delete all chars to make empty string
        for i in range(1, m + 1):
            compute_cost[i][0] = compute_cost[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            compute_cost[0][j] = compute_cost[0][j-1] + ord(s2[j-1])
        
        # Fill the remaining cells using the Bellman Equation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the chars are the same no deletion needed from upper left
                if s1[i-1] == s2[j-1]:
                    compute_cost[i][j] = compute_cost[i-1][j-1]
                # Chars aren't the same so either delete from s1 or s2
                else:
                    compute_cost[i][j] = min(
                        ord(s1[i-1]) + compute_cost[i-1][j],
                        ord(s2[j-1]) + compute_cost[i][j-1]
                    )

        # Return the answer for entire input strings
        return compute_cost[m][n]

test_cases = [
    [231, "sea", "eat"],
    [403, "delete", "leet"]
]
solution = Solution()
for expected, s1, s2 in test_cases:
    actual = solution.minimumDeleteSum(s1, s2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s1: {s1}, s2: {s2}")

print("Ran all tests")
