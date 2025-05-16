from typing import List


class Solution:
    # Dp see what longest sequence that ends at i is, then backtrack
    # Time O(n^2 * L) where n is len words and L is length of each word
    # Space O(n)
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        # Longest subsequence that can end at this index
        dp = [1] * n
        # Index that preceeds this in longest sequence
        prev_index = [-1] * n
        max_index = 0
        longest = 1

        for end in range(n):
            end_group = groups[end]
            end_word = words[end]
            for prev in range(end):
                prev_word = words[prev]
                # See if this word should be added
                if (
                    groups[prev] == end_group
                    or dp[prev] < dp[end]
                    or not self._check_word_qualifies(prev_word, end_word)
                ):
                    continue

                # Add the word
                dp[end] = dp[prev] + 1
                prev_index[end] = prev

                # Update longest if needed
                if dp[end] > longest:
                    longest = dp[end]
                    max_index = end

        # backtrack and build answer
        answer = []
        while max_index != -1:
            answer.append(words[max_index])
            max_index = prev_index[max_index]

        # Reverse since it's backwards now
        answer.reverse()
        return answer
    
    def _check_word_qualifies(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        distance = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                distance += 1
                if distance > 1:
                    return False

        return distance == 1

    
test_cases = [
    [["bab","dab"], ["bab","dab","cab"], [1,2,2]],
    [["a","b","c","d"], ["a","b","c","d"], [1,2,3,4]]
]
solution = Solution()
for expected, words, groups in test_cases:
    actual = solution.getWordsInLongestSubsequence(words, groups)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words: {words}, groups: {groups}")

print("Ran all tests")