from collections import defaultdict


class Solution:
    # Sliding window of how many in a given candy
    # Time O(n)
    # Space O(n) as we store set of candy flavors
    def shareCandies(self, candies: list[int], k: int) -> int:
        n = len(candies)

        # Store the total number of unique flavors in the array.
        flavor_freq = defaultdict(int)
        for flavor in candies:
            flavor_freq[flavor] += 1

        # Get the total number of unique flavors in the array.
        unique_flavors = len(flavor_freq)

        # Get the flavors used completely in the window.
        used_in_window = 0
        for i in range(k):
            flavor_freq[candies[i]] -= 1
            if flavor_freq[candies[i]] == 0:
                used_in_window += 1

        # Get the flavors in the remaining array currently.
        max_flavors = unique_flavors - used_in_window

        # Slide the window to the right and update counts
        for i in range(k, n):
            # Remove the old flavor from the window
            old_flavor = candies[i-k]
            flavor_freq[old_flavor] += 1
            if flavor_freq[old_flavor] == 1:
                used_in_window -= 1

            # Add the new flavor to the window
            new_flavor = candies[i]
            flavor_freq[new_flavor] -= 1
            if flavor_freq[new_flavor] == 0:
                used_in_window += 1

            max_flavors = max(max_flavors, unique_flavors - used_in_window)

        return max_flavors

test_cases = [
    [3, [1,2,2,3,4,3], 3],
    [2, [2,2,2,2,3,3], 2],
    [3, [2,4,5], 0]
]
solution = Solution()
for expected, candies, k in test_cases:
    actual = solution.shareCandies(candies, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: candies: {candies}, k: {k}")

print("Ran all tests")
