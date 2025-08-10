class Solution:
    # This problem is stupid. The real solution would be gen perms of n
    # And see if they are a power of 2, but that would be n! (digits of n!)
    # So instead we know the problem bounds n to less than 10^9 so we just compute
    # All the powers of 2 less than that and sort them and see if n sorted equals any of those
    # Time O(logn)
    # Space O(logn)
    def reorderedPowerOf2(self, n: int) -> bool:
        # Sorts the digits of the number x
        def sort_digits(x: int) -> str:
            return ''.join(sorted(str(x)))

        # Find the target we are looking for
        target = sort_digits(n)
        
        # Go through all powers of 2 less than 10^9 and see if equal
        for i in range(31):
            if sort_digits(1 << i) == target:
                return True
            
        # None are so return false
        return False
    
test_cases = [
    [True, 1],
    [False, 10]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.reorderedPowerOf2(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")