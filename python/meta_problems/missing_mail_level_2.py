from typing import List


# DP to compute expected values and work backwards from end to see what you should do
# Time O(n^2)
# Space O(n^2)
def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    prob_packages_remain = 1 - S
    max_profit = [[0] * (N + 1) for _ in range(N + 1)]
    expected_mail_value = [[0] * (N + 1) for _ in range(N + 1)]

    # Precompute the expected_mail_value lookup table.
    for j in range(N):
        # On that day you know it will have exactly that value
        expected_mail_value[j][j] = V[j]
        # Now for all days after it, compute as if this package was left
        for i in range(j + 1, N):
            expected_mail_value[i][j] = V[i] + (expected_mail_value[i - 1][j] * prob_packages_remain)

    # Work backwards from the end and decide if you should take a package at a day or not
    for i in range(N - 1, -1 , -1):
        for j in range(i, -1, -1):
            # Max of take the package today or not
            max_profit[i][j] = max(max_profit[i+1][i+1] + expected_mail_value[i][j] - C,
                                   max_profit[i+1][j])

    # Max profit on day zero
    return max_profit[0][0]

test_cases = [
    [25.0, 5, [10, 2, 8, 6, 4], 5, 0.0],
    [9.0, 5, [10, 2, 8, 6, 4], 5, 1.0],
    [17.0, 5, [10, 2, 8, 6, 4], 3, 0.5],
    [20.1, 5, [10, 2, 8, 6, 4], 3, 0.15]
]
for expected, N, V, C, S in test_cases:
    actual = round(getMaxExpectedProfit(N, V, C, S), 1)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: N: {N}, V: {V}, C: {C}, S: {S}")

print("Ran all tests")