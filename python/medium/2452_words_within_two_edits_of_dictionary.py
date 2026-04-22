class Solution:
    # Just go over each word in queries and test against each dictionary word
    # Time O(qL*dL)
    # Space O(1)
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        L = len(queries[0])
        answer = []

        # Go over all words in query
        for word in queries:
            # See if they match with any dictionary word
            for dict_word in dictionary:
                mismatch = 0

                # Go over full word and see if match
                for i in range(L):
                    if word[i] != dict_word[i]:
                        mismatch += 1

                    if mismatch > 2:  # noqa: PLR2004
                        break

                if mismatch <= 2:  # noqa: PLR2004
                    answer.append(word)
                    # No need to check rest of dictionary words, we know this matches
                    break

        return answer

test_cases = [
    [["word","note","wood"], ["word","note","ants","wood"], ["wood","joke","moat"]],
    [[], ["yes"], ["not"]]
]
solution = Solution()
for expected, queries, dictionary in test_cases:
    actual = solution.twoEditWords(queries, dictionary)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: queries: {queries}, dictionary: {dictionary}")

print("Ran all tests")
