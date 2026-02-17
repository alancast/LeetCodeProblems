class Solution:
    # Time O(n) as we just go through nums once
    # Space O(1) all that's used is answer space
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        answer = []
        already_used = -1

        # Loop over all numbers, if key is found make sure indexes +- k are added
        for index, num in enumerate(nums):
            if num == key:
                for i in range(max(already_used + 1, index - k), min(n, index + k + 1)):
                    answer.append(i)
                    already_used = i


        return answer

test_cases = [
    [[1,2,3,4,5,6], [3,4,9,1,3,9,5], 9, 1],
    [[0,1,2,3,4], [2,2,2,2,2], 2, 2]
]
solution = Solution()
for expected, nums, key, k in test_cases:
    actual = solution.findKDistantIndices(nums, key, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: nums: {nums}, key: {key}, k: {k}")

print("Ran all tests")
