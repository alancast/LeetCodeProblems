from collections import deque


class Solution:
    # O(log(target)) time O(1) space
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2 == 1: 
                target += 1
            else: 
                target //= 2

        return ans + startValue - target

    # Iterative push to queue until answer shows up
    def brokenCalcTooSlow(self, startValue: int, target: int) -> int:
        queue = deque([(startValue, 0)])
        checked = set()
        while queue:
            value, count = queue.popleft()
            if value in checked:
                continue

            if value == target:
                return count
            queue.append((value * 2, count + 1))
            queue.append((value - 1, count + 1))

testCases = [
    [2, 3, 2],
    [5, 8, 2],
    [3, 10, 3]
]
implementation = Solution()
for startValue, target, expected in testCases:
    answer = implementation.brokenCalc(startValue, target)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: startValue: {startValue} target: {target}")