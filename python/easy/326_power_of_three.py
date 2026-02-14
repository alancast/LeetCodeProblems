class Solution:
    # Turns out you can math this with the largest power of 3 that fits into int
    # Take that (3^19) and make sure it mod this number is 0, that gives your answer
    # Time O(1)
    # Space O(1)
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

    # Time O(logn)
    # Space O(1)
    def isPowerOfThree_normal_human_way(self, n: int) -> bool:
        # Make sure number is > 0
        if n < 1:
            return False

        # Make sure it's always divisible by 3 and then divide by 3
        while n > 1:
            if n % 3 != 0:
                return False

            n //= 3

        # If we got here that means n is 1 so it is a power of 3
        return True

test_cases = [
    [True, 27],
    [False, 0],
    [False, -1]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.isPowerOfThree(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")
