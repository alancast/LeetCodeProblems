from collections import Counter


class Solution:
    # Counter and then see what numbers can be made
    # Time O(n)
    # Space O(1) (n but effectively 10 since all single digits)
    def totalNumbers(self, digits: list[int]) -> int:
        f = Counter(digits)

        answer = 0
        # Go over all 3 digit even numbers and see if we can make it
        for n in range(100, 1000, 2):
            # Get hundreds digit
            i, rem = divmod(n, 100)
            # Get 10's digit
            j, k = divmod(rem, 10)
            answer += f[i] > 0 and f[j] > (i == j) and f[k] > (i == k) + (j == k)

        return answer

test_cases = [
    [12, [1,2,3,4]],
    [2, [0,2,2]],
    [1, [6,6,6]],
    [0, [1,3,5]]
]
solution = Solution()
for expected, digits in test_cases:
    actual = solution.totalNumbers(digits)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: digits: {digits}")

print("Ran all tests")
