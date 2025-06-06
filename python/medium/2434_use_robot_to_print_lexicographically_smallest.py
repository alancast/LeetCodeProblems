from collections import Counter


class Solution:
    # Same exact logic as below but cleaner
    # Time O(n) as we process every letter once and do a bunch of O(1) operations with it
    # Space O(n)
    def robotWithString(self, s: str) -> str:
        # O(n) as go through full s for counting
        char_counts = Counter(s)
        
        t = []
        answer = []
        minCharacter = "a"

        # Go through every char in S and process it
        for char in s:
            # Default put char in t
            t.append(char)
            char_counts[char] -= 1

            # find the min char left in s
            while minCharacter != "z" and char_counts[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)

            # Put all of t into the answer until there is a letter in S left smaller
            while t and t[-1] <= minCharacter:
                answer.append(t.pop())
    
        return ''.join(answer)

    # Time O(n) as we process every letter once and do a bunch of O(1) operations with it
    # Space O(n)
    def robotWithString_dirty(self, s: str) -> str:
        letter_counts = [0] * 26
        for char in s:
            letter_counts[ord(char) - ord('a')] += 1

        t = []
        count_index = s_index = 0
        answer = ""
        while True:
            # find what letter we should be looking for
            while count_index < 26 and letter_counts[count_index] == 0:
                count_index += 1

            # if count index == 26 we have gone through string so append t backwards
            if count_index == 26:
                t_str = ''.join(reversed(t))
                return answer + t_str
            
            # compare what's smaller, count_index or the end of t (if there is anything in t)
            t_val = float('inf')
            if len(t) > 0:
                t_val = ord(t[-1]) - ord('a')

            # End of t is smaller so append it
            if t_val <= count_index:
                answer += t.pop()
            # Still a letter in s left smaller
            else:
                s_char = s[s_index]
                s_val = ord(s_char) - ord('a')
                letter_counts[s_val] -= 1
                if s_val == count_index:
                    answer += s_char
                else:
                    t.append(s_char)

                s_index += 1
    
test_cases = [
    ["azz", "zza"],
    ["abc", "abc"],
    ["abc", "bac"],
    ["addb", "bdda"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.robotWithString(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")