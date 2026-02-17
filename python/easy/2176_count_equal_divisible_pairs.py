from collections import defaultdict


class Solution:
    # Go through list and create a map of nums to index list
    # Each time we see a num already in there see if index products are divisible by k
    # Time O(n^2) as worst case they are all the same number so we go through whole list each time
    # Space O(n) as we have a map copy basically
    def countPairs(self, nums: list[int], k: int) -> int:
        num_to_index_list_map = defaultdict(list)
        good_pairs = 0

        for i, num in enumerate(nums):
            for index in num_to_index_list_map[num]:
                product = i * index
                if product % k == 0:
                    good_pairs += 1

            num_to_index_list_map[num].append(i)

        return good_pairs

test_cases = [
    [4, [3,1,2,2,2,1,3], 2],
    [0, [1,2,3,4], 1]
]
solution = Solution()
for expected, nums, k in test_cases:
    actual = solution.countPairs(nums, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}, k: {k}")

print("Ran all tests")
