from typing import List


class Solution:
    # Math basically. A number has 4 divisors if one of the two is true
    # Case 1: p^3
    # Case 2: p×q (Where p and q are two distinct primes)
    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0

        # Go over all nums and see if it is a 4 divisor num and if so add
        for num in nums:
            # If this is a number that should be added include it
            val = self._sumOne(num)
            if val != -1:
                answer += val

        return answer

    # Checks if the number is one of the valid types of four divisor
    # Returns the sum of the divisors if it is, if not returns -1
    def _sumOne(self, num: int) -> int:
        p = round(num ** (1/3))
        if p ** 3 == num and self._isPrime(p):
            return 1 + p + p*p + p*p*p

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                a = i
                b = num // i
                if a != b and self._isPrime(a) and self._isPrime(b):
                    return 1 + a + b + num
                return -1
    
        return -1

    # See if a number is prime
    def _isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

test_cases = [
    [32, [21, 4, 7]],
    [64, [21, 21]],
    [0, [1, 2, 3, 4, 5]]
]
solution = Solution()
for expected, nums in test_cases:
    actual = solution.sumFourDivisors(nums)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: nums: {nums}")

print("Ran all tests")