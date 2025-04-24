from typing import List
from math import floor


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        self._validate_input(left, right)
        return self._closest_primes_twin_primes(left, right)

    # Some magic BS that in a range of 1452 or less there is guaranteed to be a twin prime
    # Twin prime is two primes off by 2. So if range is > 1452 we just find first twin primes
    # If less than we compute primes manually
    # Time O(min(1452, r - l) * sqrt r)
    # Space O(1)
    def _closest_primes_twin_primes(self, left: int, right: int) -> List[int]:
        answer = [-1, -1]
        primes = []
        min_diff = float("inf")
        for i in range(left, right + 1):
            if self._is_prime(i):
                if len(primes) > 0:
                    diff = i - primes[-1]
                    if diff < min_diff:
                        min_diff = diff
                        answer[0] = primes[-1]
                        answer[1] = i
                    if diff == 1 or diff == 2:
                        return answer
                
                primes.append(i)

        return answer

    # Create a list of prime numbers and then go through it that way
    # Time O(r log r)
    # Space O(r)
    def _closest_primes_sieve(self, left: int, right: int) -> List[int]:
        # List of prime numbers. Each index is whether that number is prime or not
        sieve = self._create_sieve(right + 1)

        # Now find the min difference in the range
        answer = [-1, -1]
        primes = []
        min_diff = float("inf")
        for i in range(left, right + 1):
            if sieve[i]:
                if len(primes) > 0:
                    diff = i - primes[-1]
                    if diff < min_diff:
                        min_diff = diff
                        answer[0] = primes[-1]
                        answer[1] = i
                
                primes.append(i)

        return answer
    
    def _create_sieve(self, upper_bound: int) -> List[bool]:
        # List of prime numbers. Each index is whether that number is prime or not
        sieve = [True] * upper_bound
        sieve[0] = False
        sieve[1] = False
        # Go through and mark all multiples as not prime
        limit = int(pow(upper_bound, 0.5)) + 1
        for i in range(2, limit):
            temp = i + i
            while temp < upper_bound:
                sieve[temp] = False
                temp += i

        return sieve

    # Time limit exceeds
    # Time O(n sqrt n)
    # Space O(n)
    def _closest_primes_brute_force(self, left: int, right: int) -> List[int]:
        answer = [-1, -1]
        primes = []
        min_diff = float("inf")
        for i in range(left, right + 1):
            if self._is_prime(i):
                if len(primes) > 0:
                    diff = i - primes[-1]
                    if diff < min_diff:
                        min_diff = diff
                        answer[0] = primes[-1]
                        answer[1] = i
                
                primes.append(i)

        return answer
    
    # Time O(sqrt n)
    def _is_prime(self, num: int) -> bool:
        upper_bound = floor(pow(num, 0.5)) + 1
        for i in range(2, upper_bound):
            if num % i == 0:
                return False
        
        return num > 1
    
    def _validate_input(self, left: int, right: int) -> None:
        if left > right:
            raise ValueError("left must be less than right")
        if left < 1 or left > pow(10, 6):
            raise ValueError("left must be between 1 and 10^6")
        if right < 1 or right > pow(10, 6):
            raise ValueError("right must be between 1 and 10^6")
        

test_cases = [
    [[11,13], 10, 19],
    [[-1,-1], 4, 6],
    [[2,3], 1, 100000],
    [[2,3], 1, 4]
]
solution = Solution()
for expected, left, right in test_cases:
    actual = solution.closestPrimes(left, right)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: left: {left}, right: {right}")

print("Ran all tests")