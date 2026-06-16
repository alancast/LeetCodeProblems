class Solution:
    # Just do the process brute force
    # Time O(2^n) as worst case duplicate and reverse entire string each time
    # Space O(1)
    # or 2^n, I mean all that's stored is answer but that could be large then shrink
    # And technically reverse has a temp string of same size so 2^n is more right
    def processStr(self, s: str) -> str:
        answer = []
        for char in s:
            if char == "#":
                answer += answer
            elif char == "%":
                answer.reverse()
            elif char == "*":
                if answer:
                    answer.pop()
            else:
                answer.append(char)

        return "".join(answer)

test_cases = [
    ["ba", "a#b%*"],
    ["", "*"],
    ["", "z*#"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.processStr(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")
