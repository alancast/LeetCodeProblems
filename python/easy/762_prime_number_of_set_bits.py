class Solution:
    # Just go over all items in range from left to right and see if they fit
    # Time O(range)
    # Space O(1)
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # All the prime numbers less than 32 (which is max bits in int)
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        # Go over all numbers in range and see if they should be counted
        answer = 0
        for num in range(left, right+1):
            if bin(num).count('1') in primes:
                answer += 1

        return answer

test_cases = [
    [4, 6, 10],
    [5, 10, 15]
]
solution = Solution()
for expected, left, right in test_cases:
    actual = solution.countPrimeSetBits(left, right)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: left: {left}, right: {right}")

print("Ran all tests")
