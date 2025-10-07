from bisect import bisect_right
from typing import List


class Solution:
    # Go over list and keep track of full lakes and rainless days
    # once we see a lake that is already full we retroactively dry it
    # Pick which day to dry with binary search
    # Time O(nlogn)
    # Space O(n)
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        
        # Initialize all days to no drying
        answer = [1] * n

        # Queue of days where we can dry a lake (for updating array)
        dry_days = []
        # Map of what lake is full and what day it got full
        full_lakes = dict()
        for i in range(n):
            lake = rains[i]

            # No rain so have a dry day we can update later
            if lake == 0:
                dry_days.append(i)
                continue
            
            # It's raining somewhere, see if there is a flood or not
            else:
                answer[i] = -1
                # Lake is going from dry to full
                if lake not in full_lakes:
                    full_lakes[lake] = i
                    continue

                # Lake is already full, see if it's possible to dry
                if lake in full_lakes:
                    # Binary search to find smallest day after day it was filled
                    # Where it can be dried
                    dry_day = bisect_right(dry_days, full_lakes[lake])

                    # If no dry day after it was filled impossible to avoid flood
                    # So return empty array
                    if dry_day == len(dry_days):
                        return []
                    
                    # Dry the lake on that day
                    answer[dry_days[dry_day]] = lake

                    # Update the data structures, remove the dry day and update lake filling day
                    dry_days.pop(dry_day)
                    full_lakes[lake] = i

        return answer

test_cases = [
    [[-1,-1,-1,-1], [1,2,3,4]],
    [[-1,1,-1,2,-1,-1], [1,0,2,0,1,2]],
    [[-1,-1,2,1,-1,-1], [1,2,0,0,2,1]],
    [[-1,69,1,1,-1], [69,0,0,0,69]],
    [[], [1,2,0,1,2]]
]
solution = Solution()
for expected, rains in test_cases:
    actual = solution.avoidFlood(rains)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: rains: {rains}")

print("Ran all tests")