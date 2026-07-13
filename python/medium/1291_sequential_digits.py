class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        return []

test_cases = [
    [[123,234], 100, 300],
    [[1234,2345,3456,4567,5678,6789,12345], 1000, 13000]
]
solution = Solution()
for expected, low, high in test_cases:
    actual = solution.sequentialDigits(low, high)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: low: {low}, high: {high}")

print("Ran all tests")
