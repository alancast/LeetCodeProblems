from typing import List


class Solution:
    # Take top n batteries and use them for computers
    # Keep using up extra power until you can no longer get to next level
    # Time O(nlogn)
    # Space O(n)
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Get the sum of all extra batteries.
        batteries.sort()   
        extra = sum(batteries[:-n])
        
        # The n largest batteries we chose for n computers.
        live = batteries[-n:]
        
        # Increase the total running time using 'extra' by increasing 
        # the running time of the computer with the smallest battery.
        for i in range(n - 1):
            # If we can't get to the next power level needed
            if (extra // (i + 1)) < (live[i + 1] - live[i]):
                # Return how close we can get
                return live[i] + (extra // (i + 1))
            
            # Reduce 'extra' by the total power used.
            # Must add to i+1 computers, hence the multiplication
            extra -= (i + 1) * (live[i + 1] - live[i])
        
        # If there is power left, we can increase the running time of all computers.
        return live[-1] + (extra // n)

    # Binary Search of running time
    # Sum up how much extra can be distributed 
    # Time O(n + nlogk) k is max battery power
    # Space O(1)
    def maxRunTime_binary_search(self, n: int, batteries: List[int]) -> int:
        left = 1
        right = sum(batteries) // n
        
        # Binary search for target numbers
        while left <= right:
            target = (right + left) // 2
            
            # Figure out how much extra battery there is
            extra = 0
            for power in batteries:
                # No need to go above target (breaks logic)
                extra += min(power, target)
            
            if extra // n >= target:
                left = target + 1
            else:
                right = target - 1
        
        return right

test_cases = [
    [4, 2, [3,3,3]],
    [2, 2, [1,1,1,1]],
    [8, 3, [10,10,3,5]]
]
solution = Solution()
for expected, n, batteries in test_cases:
    actual = solution.maxRunTime(n, batteries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, batteries: {batteries}")

print("Ran all tests")