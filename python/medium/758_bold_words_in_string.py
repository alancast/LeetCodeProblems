class Solution:
    # Go over each word and bold it every time it appears
    # Then go over and see what should be bolded
    # Time O(w*n) w is length of words, n is length of s
    # Space O(n)
    def boldWords(self, words: list[str], S: str) -> str:
        n = len(S)

        # Create a mapping of if each char is bold or not
        bold = [False] * n

        # Go over each word and find each time it appears in S
        # When it does mark it as bolded
        for word in words:
            start = 0
            # Keep incrementing start so we get every instance of word in string
            while start < n:
                idx = S.find(word, start)
                if idx >= 0 :
                    bold[idx:idx+len(word)] = [True] * len(word)
                    start = idx + 1
                else:
                    break

        # Go over S and see when to add and remove a bold
        result = []
        for i, c in enumerate(S):
            # Add a bold if this char is bolded and one before it isn't
            if bold[i] and (i == 0 or not bold[i - 1]):
                result.append('<b>')

            # Append the letter
            result.append(c)

            # If next is not bolded but this was, add an end bold
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                result.append('</b>')

        # Make new answer string
        return "".join(result)

test_cases = [
    ["a<b>abc</b>d", ["ab","bc"], "aabcd"],
    ["a<b>ab</b>cd", ["ab","cb"], "aabcd"]
]
solution = Solution()
for expected, words, S in test_cases:
    actual = solution.boldWords(words, S)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, S: {S}")

print("Ran all tests")
