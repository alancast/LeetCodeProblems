class Solution:
    def oneStringSwap(self, s1: str, s2: str) -> bool:
        # If they are different lengths it's impossible
        if len(s1) != len(s2):
            return False

        # Go through the strings and make sure at most 2 differences
        # Store the differences letter as it needs to be the correct letter as well
        diffChar1 = ''
        diffChar2 = ''
        numDiffs = 0
        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]
            if char1 == char2:
                continue

            # the chars aren't the same
            # If this is the first time store the diff
            # If second time check the diff
            # If third time the strings don't work
            numDiffs += 1
            if numDiffs == 1:
                diffChar1 = char1
                diffChar2 = char2
            elif numDiffs == 2:  # noqa: PLR2004
                if char2 != diffChar1 or char1 != diffChar2:
                    return False
            elif numDiffs == 3:  # noqa: PLR2004
                return False

        # We got through all the chars of the string
        # If there was only 1 diff they aren't swappable, if 0 or 2 they are
        return numDiffs != 1

testCases = [
    ["bank", "kanb", True],
    ["", "", True],
    ["attack", "defend", False],
    ["ba", "ab", True],
    ["aa", "ab", False],
    ["abc", "cbd", False],
    ["kelb", "kelb", True]
]
solution = Solution()
for s1, s2, expected in testCases:
    answer = solution.oneStringSwap(s1, s2)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Inputs: s1: {s1} s2: {s2}")

print("Ran all tests")
