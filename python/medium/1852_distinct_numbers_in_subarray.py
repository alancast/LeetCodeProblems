from collections import defaultdict
from typing import List


class Solution:
    # Time O(n) as we just go through nums once
    # Space O(k) as we have a dictionary of length k
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []
        num_counts = defaultdict(int)

        # create first subarray of length k
        for i in range(k):
            num_counts[nums[i]] += 1
        answer.append(len(num_counts))

        # Remove first num and add next
        for i in range(n - k):
            old_num = nums[i]
            new_num = nums[i+k]

            num_counts[old_num] -= 1
            if num_counts[old_num] == 0:
                del num_counts[old_num]

            num_counts[new_num] += 1
            answer.append(len(num_counts))

        return answer
    
test_cases = [
    [[3,2,2,2,3], [1,2,3,2,2,1,3], 3],
    [[1,2,3,4], [1,1,1,1,2,3,4], 4]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.distinctNumbers(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}.")
        print(f"\tINPUTS: nums: {nums}, k: {k}")

print("Ran all tests")