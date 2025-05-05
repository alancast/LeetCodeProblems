class Solution:
    # Dynamic programming with math
    # The key equation is f(n) = f(n - 1) + f(n - 2) + 2 * p(n - 1) 
    # and p(n) = p(n-1) + f(k-2)
    # There a time log(n) solution with matrix math
    # And another solution that removes p with math so it's only in terms of f
    # Time O(n)
    # Space O(1)
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        MOD = 1_000_000_007

        prev_partial = 1
        full = prev_full = 2
        full_minus_2 = 1

        for i in range(3, n + 1):
            full = (prev_full + full_minus_2 + (2* prev_partial)) % MOD
            prev_partial = (prev_partial + full_minus_2) % MOD
            full_minus_2 = prev_full
            prev_full = full

        return full

    # Dynamic programming with math
    # The key equation is f(n) = f(n - 1) + f(n - 2) + 2 * p(n - 1)
    # Time O(n)
    # Space O(n)
    def numTilings_dynamic_programming_not_optimized(self, n: int) -> int:
        if n == 1:
            return 1
        
        MOD = 1_000_000_007

        partial = [0] * (n + 1)
        full = [0] * (n + 1)
        full[1] = 1
        full[2] = 2
        partial[2] = 1

        for i in range(3, n + 1):
            full[i] = (full[i-1] + full[i-2] + (2 * partial[i-1])) % MOD
            partial[i] = (partial[i-1] + full[i-2]) % MOD

        return full[n]
    
test_cases = [
    [5, 3],
    [1,1]
]
solution = Solution()
for expected, n in test_cases:
    actual = solution.numTilings(n)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: n: {n}")

print("Ran all tests")