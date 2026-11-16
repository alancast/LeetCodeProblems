class Solution:
    # Use the shared item to cover the overlap, then fill the rest with the cheapest single-type option
    # Time O(1)
    # Space O(1)
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        shared = min(need1, need2)
        answer = shared * min(costBoth, cost1 + cost2)

        need1 -= shared
        need2 -= shared

        answer += need1 * min(cost1, costBoth)
        answer += need2 * min(cost2, costBoth)
        return answer

test_cases = [
    [3, 3, 2, 1, 3, 2],
    [22, 5, 4, 15, 2, 3],
    [0, 5, 4, 15, 0, 0]
]
solution = Solution()
for expected, cost1, cost2, costBoth, need1, need2 in test_cases:
    actual = solution.minimumCost(cost1, cost2, costBoth, need1, need2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: cost1: {cost1}, cost2: {cost2}, costBoth: {costBoth}, need1: {need1}, need2: {need2}")

print("Ran all tests")
