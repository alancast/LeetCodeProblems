from typing import List


class Solution:
    # Process each potion in order
    # Keep track of when each wizard is free (when they finished previous potion)
    # And use that to figure out when to start each potion
    # Time O(ms)
    # Space O(s) as we keep array of earliest free time for each skill
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        s = len(skill)
        free_times = [0] * s

        # Process each potion
        for potion in mana:

            # Find the time when this potion will end
            potion_end_time = 0
            for i in range(s):
                potion_end_time = max(potion_end_time, free_times[i]) + (skill[i] * potion)

            # Work backwards from when potion finishes to see when we start it for each wizard
            free_times[-1] = potion_end_time
            for i in range(s - 2, -1, -1):
                free_times[i] = free_times[i + 1] - (skill[i + 1] * potion)

        return free_times[-1]

test_cases = [
    [110, [1,5,2,4], [5,1,4,2]],
    [5, [1,1,1], [1,1,1]],
    [21, [1,2,3,4], [1,2]]
]
solution = Solution()
for expected, skill, mana in test_cases:
    actual = solution.minTime(skill, mana)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: skill: {skill}, mana: {mana}")

print("Ran all tests")