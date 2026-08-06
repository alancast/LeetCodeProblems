class Solution:
    # Just go over all numbers until it's right
    # Time O(10logn)
    # Space O(1)
    def smallestNumber(self, n: int, t: int) -> int:
        # See if the product of this num is divisible by t
        def check(num: int) -> bool:
            # Compute product of num
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
                if product == 0:
                    break

            # Check divisibility
            return product % t == 0

        # Increase n until it's right
        while not check(n):
            n += 1

        return n

test_cases = [
    [10, 10, 2],
    [16, 15, 3]
]
solution = Solution()
for expected, n, t in test_cases:
    actual = solution.smallestNumber(n, t)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, t: {t}")

print("Ran all tests")
