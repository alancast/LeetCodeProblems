from collections import Counter


class Solution:
    # Counter (hash table) and enumeration
    # Time O(nlogm)
    # Space O(n) for counter
    def maximumLength(self, nums: list[int]) -> int:
        counter = Counter(nums)

        ones_count = counter.get(1, 0)

        # Answer is at least the number of occurrences of 1, rounded down to an odd number
        # Because mountain of 1 can be the answer (must be odd cuz 1 peak)
        answer = ones_count if ones_count % 2 else ones_count - 1

        # Remove 1's from the counter as they aren't needed
        counter.pop(1, None)

        # Go over all nums and see how big of mountain you can make
        for num in counter:
            result = 0
            x = num
            # Make sure there are 2 instances of x in the counter (one for up one for down)
            # Then see how high you can make the number
            while x in counter and counter[x] > 1:
                result += 2
                x *= x

            # Answer is result + 1 if can have higher peak, -1 of needs lower peak
            answer = max(answer, result + (1 if x in counter else -1))

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
