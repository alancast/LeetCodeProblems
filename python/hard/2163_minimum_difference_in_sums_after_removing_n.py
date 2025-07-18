from heapq import heappop, heappush
from typing import List


class Solution:
    # Split into 3 parts, 0-n, n-2n, 2n-3n
    # We want max nums from n - 3n and min nums from 0-2n
    # Create those two and see what solution gives the min
    # Time O(nlogn)
    # Space O(n)
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # Create the max
        max_heap = []
        total = 0
        for i in range(n):
            num = nums[i]
            total += num
            heappush(max_heap, -num)

        # The part we are trying to minimize
        part1 = [0] * (n + 1)
        part1[0] = total

        # Go over nums n - 2n and see how much we can minimize
        for i in range(n, n * 2):
            num = nums[i]

            # Add new number to heap
            total += num
            heappush(max_heap, -num)

            # Remove biggest number
            total -= -heappop(max_heap)

            # Store updated total value
            part1[i - (n - 1)] = total

        # Now work backwards and do min heap
        min_heap = []
        part2 = 0
        for i in range(2*n, 3*n):
            num = nums[i]
            part2 += num
            heappush(min_heap, num)

        # Now go backwards from nums 2n to n and find which one finds min difference
        answer = part1[n] - part2
        for i in range((n * 2) - 1, n - 1, -1):
            # Add new num to part 2
            num = nums[i]
            part2 += num
            heappush(min_heap, num)
            # Remove smallest num from part 2 and subtract
            part2 -= heappop(min_heap)

            # See if this index i is a new min answer
            answer = min(answer, part1[i - n] - part2)

        return answer
test_cases = [
    [-1, [3,1,2]],
    [1, [7,9,5,8,1,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.minimumDifference(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")