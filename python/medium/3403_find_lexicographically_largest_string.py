class Solution:
    # Move two pointers i and j
    # While the char they are comparing is the same make them both longer
    # As soon as there is a diff keep whichever one is larger
    # Time O(n) as each pointer just goes over n once
    # Space O(1 or n) depending on how substrings are handled
    # In python it's a view so O(1)
    def _get_lexicographically_largest_string(self, s: str) -> str:
        i = 0
        j = 1
        n = len(s)

        while j < n:
            # K represents the substring length
            k = 0
            # When the two pointers are equal make the word longer
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            
            # J is start of superior word, so make it the starting point
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            # J is inferior word, so move it forward and try again
            else:
                j = j + k + 1
        
        # Return the lexicographically largest string (but might be too long)
        return s[i:]

    # Time O(n) as each pointer just goes over n once
    # Space O(1 or n) depending on how substrings are handled
    # In python it's a view so O(1)
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        max_len = n - numFriends + 1

        if numFriends == 1:
            return word
        
        highest_order = self._get_lexicographically_largest_string(word)
        m = len(highest_order)
    
        # the highest order string could be too long, so we need to substring it
        return highest_order[:max_len]

    # This code is hideous and I wouldn't wish it on my worst enemy. I regret writing it
    # Time O(n) as we just go through all of the chars once (mostly)
    # Space O(n) as we store string up to length n - num_friends which could be n-1
    def answerString_GARBAGE(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        # Longest possible word with split
        max_len = n - numFriends + 1

        answer = word[0]
        i = 0
        # Iterate over word and compare chars to current answer
        while i < n-1:
            i += 1
            char = word[i]

            # New split is lexicographically greater
            if char > answer[0]:
                answer = char
                continue

            # Append answer to string if possible
            if len(answer) < max_len:
                answer += char

            # If they are the same char see which one has larger following strings
            if char == answer[0]:
                for j in range(i+1, n):
                    char_j = word[j]

                    diff = j - i
                    # We can't compare characters because out of range
                    if diff >= len(answer):
                        break

                    # See if this substring is better
                    if char_j > answer[diff]:
                        answer = word[i:j+1]
                        # if char_j can't start a new string, otherwise need to evaluate from there
                        if char_j <= char:
                            i = j
                        break
                    elif char_j < answer[diff]:
                        break

        return answer
    
test_cases = [
    ["nn", "aann", 2],
    ["zzlkwqydufmliuggnalxlbfqkoyzwg", "zpjyeuglibgfmrqilifaroybzzaomydzgjcdhtmpznomdvdiuxecfkhhuqwwhtebexryzcuqvoldjksmsolbtcxjuklvtjfyftyditlesuztlovtgeiegywjowddkoveuxxzizobweqplfctylphfpwyquqvmbtzutuciozbmfzzlkwqydufmliuggnalxlbfqkoyzwg", 89],
    ["gh", "gh", 1],
    ["dd", "ddc", 2],
    ["dc", "dbdc", 2],
    ["ddddd", "dddddd", 2],
    ["dbc", "dbca", 2],
    ["g", "gggg", 4]
]
solution = Solution()
for expected, word, numFriends in test_cases:
    actual = solution.answerString(word, numFriends)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: word: {word}, numFriends: {numFriends}")

print("Ran all tests")