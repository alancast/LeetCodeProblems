from collections import defaultdict
from typing import List


class Solution:
    # Go through each word, add it's reverse to a dictionary
    # Each time you hit a reverse add 4 and pop them
    # Time O(n) as we go through each word
    # Space O(n) as the dictionary could be all the words
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0

        # Dictionary for what words to search for for palindrome
        searching_dict = defaultdict(int)
        # Set for things that could potentially be the middle of a palindrome
        potential_middles = set()

        # Go through every word and see if it's reverse has been seen so far
        for word in words:
            rev = word[::-1]

            # Double letters, so could be middle
            if word == rev:
                potential_middles.add(word)

            # Have seen reverse already so these 4 can be included in a palindrome
            if searching_dict[word] >= 1:
                answer += 4
                searching_dict[word] -= 1

                # If this was a potential middle and it's been paired remove it from middles option
                if word in potential_middles and searching_dict[word] == 0:
                    potential_middles.remove(word)

                # Restart loop so don't add reverse to search for future as it's been paired now
                continue

            searching_dict[rev] += 1

        # If potential middle left put it in middle
        if len(potential_middles) > 0:
            answer += 2

        return answer
    
test_cases = [
    [6, ["lc","cl","gg"]],
    [8, ["ab","ty","yt","lc","cl","ab"]],
    [2, ["cc","ll","xx"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.longestPalindrome(words)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")