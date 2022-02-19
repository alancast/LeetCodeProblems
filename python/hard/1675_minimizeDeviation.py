from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    # Heap of elements. Keep popping from heap until find odd (can't divide) and compute deviation
    def minimumDeviation(self, nums: List[int]) -> int:
        if not nums:
            return 0

        evens = []
        minimum = inf
        # heapify is min_pq so we append negative version instead
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num*2)

        heapify(evens)
        min_deviation = inf
        while evens:
            current_value = -heappop(evens)
            min_deviation = min(min_deviation, current_value - minimum)
            if current_value % 2 == 0:
                minimum = min(minimum, current_value//2)
                heappush(evens, -current_value//2)
            else:
                # if the maximum is odd, break and return
                break

        return min_deviation

    # Create all possible entries for an index and then sliding window
    # Until a window gets one of each index, compute deviation and move slider
    # Do until end and return minimum
    def minimumDeviationSliding(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # pretreatment
        possible = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                temp = num
                possible.append((temp, i))
                while temp % 2 == 0:
                    temp //= 2
                    possible.append((temp, i))
            else:
                possible.append((num, i))
                possible.append((num*2, i))
        possible.sort()
        # start sliding window
        min_deviation = inf
        need_include = {i: 1 for i in range(n)}
        not_included = n
        current_start = 0

        for current_value, current_item in possible:
            need_include[current_item] -= 1
            if need_include[current_item] == 0:
                not_included -= 1
            if not_included == 0:
                while need_include[possible[current_start][1]] < 0:
                    need_include[possible[current_start][1]] += 1
                    current_start += 1
                if min_deviation > current_value - possible[current_start][0]:
                    min_deviation = current_value - possible[current_start][0]

                need_include[possible[current_start][1]] += 1
                current_start += 1
                not_included += 1

        return min_deviation

testCases = [
    [[1,2,3,4], 1],
    [[], 0],
    [[4,1,5,20,3], 3],
    [[1,1,1], 0],
    [[2,10,8], 3]
]
implementation = Solution()
for nums, expected in testCases:
    answer = implementation.minimumDeviation(nums)
    if answer != expected:
        print(f"FAILED TEST: Got {answer}, expected {expected}. Input: {nums}")