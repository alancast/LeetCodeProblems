class Solution:
    # There are a handful of bit manipulation or math ways to do this in O(1)
    # I don't care for those tricks at this point in time, the obvious way
    # Is fast enough and is understandable and readable to other engineers
    # Time O(logn)
    # Space O(1)
    def isPowerOfFour(self, n: int) -> bool:
        # Make sure number is > 0
        if n < 1:
            return False
        
        # Make sure it's always divisible by 4 and then divide by 4
        while n > 1:
            if n % 4 != 0:
                return False
            
            n //= 4

        # If we got here that means n is 1 so it is a power of 4
        return True
    
test_cases = [
    [True, 16],
    [False, 0],
    [True, 1],
    [False, -1]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.isPowerOfFour(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")