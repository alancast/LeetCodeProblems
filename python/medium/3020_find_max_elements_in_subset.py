from collections import Counter


class Solution:
    # Counter (hash table) and enumeration
    # Time O(nlogm)
    # Space O(n) for counter
    def maximumLength(self, nums: list[int]) -> int:
        counter = Counter(nums)

        ones_count = counter.get(1, 0)

        # ans is at least the number of occurrences of 1, rounded down to an odd number
        answer = ones_count if ones_count % 2 else ones_count - 1

        counter.pop(1, None)
        for num in counter:
            res = 0
            x = num
            while x in counter and counter[x] > 1:
                res += 2
                x *= x
            answer = max(answer, res + (1 if x in counter else -1))

        return answer

test_cases = [
    [3, [5,4,1,2,2]],
    [1, [1,3,2,4]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.maximumLength(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")
