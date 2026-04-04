class Solution:
    # Time O(n)
    # Space O(n)
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        n = len(encodedText)
        cols = n // rows
        answer = []

        for col in range(cols):
            j = col
            r = 0
            while r < rows and j < cols:
                answer.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(answer).rstrip()

test_cases = [
    ["cipher", "ch   ie   pr", 3],
    ["i love leetcode", "iveo    eed   l te   olc", 4],
    ["coding", "coding", 1]
]
solution = Solution()
for expected, encodedText, rows in test_cases:
    actual = solution.decodeCiphertext(encodedText, rows)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: encodedText: {encodedText}, rows: {rows}")

print("Ran all tests")
