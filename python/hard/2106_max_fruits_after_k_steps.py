from typing import List


class Solution:
    # Sliding window with running sum of things in the range
    # Have a left bound and a right bound, and a running sum of everything in that range
    # Compute how many steps taken to cover the whole range (from the starting position)
    # Time O(n) as we go over the whole array once and do O(1) operations
    # Space O(1)
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        running_sum = answer = left = right = 0

        # Returns how many steps required from starting position to cover full window
        def step(left: int, right: int) -> int:
            # Entire window to left of start
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            # Entire window to right of start
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            # Start in middle of window, so distance is min of whichever is closer to start
            # plus full range (as it's full range plus twice over whatever is closest to start)
            else:
                return (
                    min(
                        abs(startPos - fruits[right][0]),
                        abs(startPos - fruits[left][0]),
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )

        # Iterate right until it reaches the end (left will move with)
        while right < n:
            running_sum += fruits[right][1]

            # Pull left boundary up as need be
            while left <= right and step(left, right) > k:
                running_sum -= fruits[left][1]
                left += 1

            # See if this window is the winner, and iterate right
            answer = max(answer, running_sum)
            right += 1

        return answer
        
test_cases = [
    [9, [[2,8],[6,3],[8,6]], 5, 4],
    [14, [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4],
    [0, [[0,3],[6,4],[8,5]], 3, 2]
]
solution = Solution()
for expected, fruits, start_pos, k in test_cases:
    actual = solution.maxTotalFruits(fruits, start_pos, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: fruits: {fruits}, start_pos: {start_pos}, k: {k}")

print("Ran all tests")