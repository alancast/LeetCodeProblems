class Solution:
    # Can get with math
    # Time O(1)
    # Space O(1)
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        # Num2 = (k * (k + 1) * m) // 2
        # Num1 = n*(n + 1)//2 - num2
        # Num1 - num2 = n*(n + 1)//2 - 2*num2
        # Num1 - num2 = n*(n + 1)//2 - (k * (k + 1) * m)
        return (n * (n + 1) // 2) - (k * (k + 1) * m)
    
    # find sum of all multiples of m then subtract from sum formula n*n+1/2
    # Time O(n/m)
    # Space O(1)
    def differenceOfSums_additive(self, n: int, m: int) -> int:
        num2 = add = 0
        for i in range(n//m):
            add += m
            num2 += add

        num1 = ((n * (n+1))//2) - num2

        return num1 - num2
    
test_cases = [
    [19, 10, 3],
    [15, 5, 6],
    [-4, 8, 2],
    [4, 7, 2],
    [-15, 5, 1]
]
solution = Solution()
for expected, n, m in test_cases:
    actual = solution.differenceOfSums(n, m)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, m: {m}")

print("Ran all tests")