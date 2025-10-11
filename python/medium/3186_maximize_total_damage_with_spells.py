from collections import Counter
from typing import List


class Solution:
    # Sort the array then go over and see which ones to take
    # Use DP array
    # Time O(nlogn + n) for sort then going over array
    # Space O(n)
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Count each number
        power_count = Counter(power)

        # Create dictionary of power to total strength of taking that power
        strength = {k: k*power_count[k] for k in power_count}

        # Create a list of spell powers (prepended with 3 0's for bound checking)
        spells = [0, 0, 0] + sorted(list(strength.keys()))

        # Create DP array of max strength you can attain up til that spell power
        n = len(spells)
        dp = [0]*n

        # Go over all spells and see wht is max we can take
        for i in range(3, n):
            # Can we take this and last one?
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            # No? Can we take this and the one two prior?
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            # No? Guaranteed we can take the one 3 prior
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])
        
        return dp[-1]

test_cases = [
    [6, [1,1,3,4]],
    [13, [7,1,6,6]]
]
solution = Solution()
for expected, powers in test_cases:
    actual = solution.maximumTotalDamage(powers)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: powers: {powers}")

print("Ran all tests")