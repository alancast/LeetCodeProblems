class Solution:
    # Enumeration. Not a good or fun problem
    # Time O(1)
    # Space O(1)
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        answer = []
        for i in range(1024):
            h, m = (
                i >> 6,
                i & 0x3F,
            )  # Extract the high 4 bits and low 6 bits using bitwise operations

            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:  # noqa: PLR2004
                answer.append(f"{h}:{m:02d}")

        return answer

test_cases = [
    [["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"], 1],
    [[], 9]
]
solution = Solution()
for expected, turnedOn in test_cases:
    actual = solution.readBinaryWatch(turnedOn)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: turnedOn: {turnedOn}")

print("Ran all tests")
