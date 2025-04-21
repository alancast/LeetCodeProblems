class Solution:
    # Time O(logn)
    # Space O(1)
    def checkPowersOfThree(self, n: int) -> bool:
        num = 1
        # Get lowest power of 3 greater than n
        while num < n:
            num *= 3

        # Go back down to 0. If n > num then num must be in sum
        # Once num == 0 or 1 we know if it's a sum
        while num > 0 and n > 0:
            if n >= num:
                n -= num
            
            num //= 3
            
        return n == 0
    
test_cases = [
    [True, 12],
    [True, 91],
    [True, 9],
    [False, 21]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.checkPowersOfThree(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")