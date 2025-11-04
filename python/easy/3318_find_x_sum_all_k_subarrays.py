from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # Keep counts of all elements in priority queue
    # Keep a dictionary with of current count
    # Look at top of priority queue each time to compute sum
    # Time O(n * klogk)
    # Space O(k)
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        pq = []
        num_counts = defaultdict(int)
        answer = []

        for i in range(n):
            num = nums[i]
            num_counts[num] += 1
            # Min queue so need to do negatives
            heappush(pq, (-num_counts[num], -num))

            # See if we need to remove a num
            if i >= k:
                # Remove old num
                removed_num = nums[i-k]
                num_counts[removed_num] -= 1
                heappush(pq, (-num_counts[removed_num], -removed_num))

            # See if we need to add an entry into the answer
            if i >= k - 1:
                used_nums = 0
                x_sum = 0
                re_enter = set()
                # Go through queue until we have a sum to add
                while used_nums < x and pq:
                    # Peek into queue and see if num is usable
                    temp_count, temp_num = heappop(pq)
                    # This is an outdated entry or one we've already used so remove it
                    if num_counts[-temp_num] != -temp_count or (temp_count, temp_num) in re_enter:
                        continue

                    # We found the number to use, so include it and carry on
                    x_sum += (temp_num * temp_count)
                    re_enter.add((temp_count, temp_num))
                    used_nums += 1
                
                # Put the entries back in the queue
                for item in re_enter:
                    heappush(pq, item)

                answer.append(x_sum)

        return answer

test_cases = [
    [[6,10,12], [1,1,2,2,3,4,2,3], 6, 2],
    [[13,18,13,9,9], [1,5,4,4,5,2,1,4], 4, 2],
    [[13], [9,2,2], 3, 3],
    [[6], [2,2,3,3], 4, 1],
    [[6], [3,3,2,2], 4, 1],
    [[11,15,15,15,12], [3,8,7,8,7,5], 2, 2]
]
solution = Solution()
for expected, nums, k, x in test_cases:
    actual = solution.findXSum(nums, k, x)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, k: {k}, x: {x}")

print("Ran all tests")