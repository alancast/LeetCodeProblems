from collections import defaultdict


class Solution:
    # Group all nums together in hash table then compute sum once per group
    # Time O(n)
    # Space O(n)
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Create index map
        index_map = defaultdict(list[int])
        for i, num in enumerate(nums):
            index_map[num].append(i)

        # Compute answer sums
        answer = [0] * n
        for indices in index_map.values():
            # Find sum of all indices
            total = sum(indices)
            prefix_total = 0
            sz = len(indices)

            # Compute each individual entry
            for i, idx in enumerate(indices):
                answer[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx

        return answer

    # Too slow on huge nums arrays
    # Go over array twice, first time create map of indices, second time add
    # Time O(n)
    # Space O(n)
    def distance_brute_force(self, nums: list[int]) -> list[int]:
        # Create index map
        index_map = defaultdict(list[int])
        for i, num in enumerate(nums):
            index_map[num].append(i)

        # Find answer sums
        answer = []
        for i, num in enumerate(nums):
            total = 0
            for index in index_map[num]:
                total += abs(i - index)

            answer.append(total)

        return answer

test_cases = [
    [[5,0,3,4,0], [1,3,1,1,2]],
    [[0,0,0], [0,5,3]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.distance(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
