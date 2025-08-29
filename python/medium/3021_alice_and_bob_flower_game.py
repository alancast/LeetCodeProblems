class Solution:
    # I believe this is just math. The flowers need to sum to an odd number
    # So it's just odds [1,n] * evens [1,m] + evens [1,n] * odds [1,m]
    # Time O(1)
    # Space O(1)
    def flowerGame(self, n: int, m: int) -> int:
        # Turns out this even simplifies down to (n*m)//2
        evens_n = n//2
        odds_n = evens_n + (n%2)
        evens_m = m//2
        odds_m = evens_m + (m%2)

        return (odds_n * evens_m) + (odds_m * evens_n)

test_cases = [
    [3, 3, 2],
    [0, 1, 1]
]
solution = Solution()
for expected, n, m in test_cases:
    actual = solution.flowerGame(n, m)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, m: {m}")

print("Ran all tests")