class Solution:
    # Bit manipulation to do all combinations
    # Time O(n*2^n)
    # Space O(1)
    def generateAbbreviations(self, word: str) -> list[str]:
        N = len(word)
        abbreviations = []

        for mask in range(1 << N):
            curr_word = []
            abbreviated_count = 0

            for index in range(N):
                # If the bit at the position index is 1, increment the abbreviated substring.
                if mask & (1 << index):
                    abbreviated_count += 1
                else:
                    # Append the last substring and then the current character.
                    if abbreviated_count > 0:
                        curr_word.append(str(abbreviated_count))
                        abbreviated_count = 0
                    curr_word.append(word[index])

            if abbreviated_count > 0:
                curr_word.append(str(abbreviated_count))

            abbreviations.append("".join(curr_word))

        return abbreviations

test_cases = [
    [["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"], "word"],
    [["1","a"], "a"]
]
solution = Solution()
for expected, word in test_cases:
    actual = solution.generateAbbreviations(word)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}")

print("Ran all tests")
