class Solution:
    # Use counting sort, which takes more space but is linear in time
    # Naive sort below also works
    # Counting sort finds max, then creates array of size max and increments count
    # Then go over that until you have no more money
    # Time O(n+max)
    # Space O(max)
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        # Find max cost in array
        m = max(costs)

        # Update frequencies of each cost
        cost_freqs = [0] * (m + 1)
        for cost in costs:
            cost_freqs[cost] += 1

        # Go over all cost frequencies until no coins left
        answer = 0
        for cost in range(1, m + 1):
            # No ice cream cost this cost
            if not cost_freqs[cost]:
                continue

            # Can't afford to buy this ice cream
            if coins < cost:
                break

            # Count how many of this cost we can buy
            count = min(cost_freqs[cost], coins // cost)

            # Buy them
            coins -= cost * count
            answer += count

        return answer

    # Basic sort and greedy implementation
    # Time O(nlogn)
    # Space O(logn) for sort
    def maxIceCream_naive_sort(self, costs: list[int], coins: int) -> int:
        costs.sort()

        answer = 0
        for cost in costs:
            if coins < cost:
                return answer

            answer += 1
            coins -= cost

        return answer

test_cases = [
    [4, [1,3,2,4,1], 7],
    [0, [10,6,8,7,7,8], 5],
    [6, [1,6,3,1,2,5], 20]
]
solution = Solution()
for expected, costs, coins in test_cases:
    actual = solution.maxIceCream(costs, coins)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: costs: {costs}, coins: {coins}")

print("Ran all tests")
