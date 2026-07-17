class Solution:
    # Sliding window over the digits and lengths
    # Time O(64) outer loop 8, inner loop 8
    # Space O(1)
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        digits = "123456789"
        answer = []

        # Go from lowest possible length to highest possible
        for length in range(len(str(low)), len(str(high)) + 1):
            # Find starting char and see if num is above threshold
            for start_digit in range(10 - length):
                num = int(digits[start_digit: start_digit + length])

                # Make sure this num is within the range then add it
                if num >= low and num <= high:
                    answer.append(num)

        return answer

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
