class Solution:
    # Sort the costs and then just skip every third
    # Time O(nlogn)
    # Space O(logn) for sort
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)

        answer = 0
        for i, price in enumerate(cost):
            # Skip every third
            if (i + 1) % 3 == 0:
                continue

            answer += price

        return answer

test_cases = [
    [5, [1,2,3]],
    [23, [6,5,7,9,2,2]],
    [10, [5,5]]
]
solution = Solution()
for expected, cost in test_cases:
    actual = solution.minimumCost(cost)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: cost: {cost}")

print("Ran all tests")
