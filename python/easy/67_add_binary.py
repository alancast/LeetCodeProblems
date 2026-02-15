class Solution:
    # Go over string adding and then reverse
    # Time O(n)
    # Space O(1) just return string
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))

        # Make sure both strings are same size
        a = a.zfill(n)
        b = b.zfill(n)

        # Add the strings
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")

            carry //= 2

        if carry == 1:
            answer.append("1")

        # Answer is backwards so must reverse
        answer.reverse()

        return "".join(answer)

test_cases = [
    ["100", "11", "1"],
    ["10101", "1010", "1011"]
]
solution = Solution()
for expected, a, b in test_cases:
    actual = solution.addBinary(a, b)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: a: {a}, b: {b}")

print("Ran all tests")
