from typing import List


class Solution:
    # Go over array with two pointers, 
    # As soon as there is a 3rd fruit see how long current spree is
    # And move left pointer
    # Time O(n) as we go over the list once
    # Space O(1) as we keep a hash map of exactly 2 keys
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = answer = 0
        # Map of fruit to most recent index
        most_recent_map = {}

        # Go over all the fruits and see how long the current streak is
        for i in range(n):
            fruit = fruits[i]

            # We already have 2 fruits in the map that aren't this, remove one
            if fruit not in most_recent_map and len(most_recent_map) > 1:
                # Find which fruit occurred least recently and remove that one
                remove_key = 0
                remove_value = float('inf')
                for key, value in most_recent_map.items():
                    if value < remove_value:
                        remove_key = key
                        remove_value = value
                
                # Remove that fruit and add the new one
                left = most_recent_map[remove_key] + 1
                del most_recent_map[remove_key]

            # Add this fruit to the most recent map
            most_recent_map[fruit] = i

            answer = max(i - left + 1, answer)

        return answer
    
test_cases = [
    [3, [1,2,1]],
    [3, [0,1,2,2]],
    [4, [1,2,3,2,2]]
]
solution = Solution()
for expected, fruits in test_cases:
    actual = solution.totalFruit(fruits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: fruits: {fruits}")

print("Ran all tests")