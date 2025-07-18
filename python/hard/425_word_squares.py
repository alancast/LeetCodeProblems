from collections import defaultdict
from typing import List


class Solution:
    # Use a Trie in this one
    # Time O(N*26^L)
    # Space O(N*L)
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        self._build_trie(self.words)

        results = []
        # Try every word as start word
        for word in words:
            word_squares = [word]
            self._backtrack(1, word_squares, results)

        return results
    
    def _build_trie(self, words: List[str]) -> None:
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def _backtrack(self, step: int, word_squares: List[str], results: List[List[str]]) -> None:
        # If we have reached the end this is a valid solution
        if step == self.N:
            results.append(word_squares[:])
            return
        
        # Attempt words for next step
        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self._get_words_with_prefix(prefix):
            word_squares.append(candidate)
            self._backtrack(step+1, word_squares, results)
            word_squares.pop()

    def _get_words_with_prefix(self, prefix: str) -> List[str]:
        node = self.trie

        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        
        # Return the index of all the words
        return [self.words[wordIndex] for wordIndex in node['#']]

    # Backtracking with hash table of prefixes
    # Time O(N*26^L)
    # Space O(N*L) hash table each N words appears L times
    def wordSquares_hash_table_backtrack(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        self._build_prefix_hash(words)

        results = []
        # Try every word as start word
        for word in words:
            word_squares = [word]
            self._backtrack_hash(1, word_squares, results)

        return results

    def _backtrack_hash(self, step: int, word_squares: List[str], results: List[List[str]]) -> None:
        # If we have reached the end this is a valid solution
        if step == self.N:
            results.append(word_squares[:])
            return
        
        # Attempt words for next step
        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.prefix_hash[prefix]:
            word_squares.append(candidate)
            self._backtrack_hash(step+1, word_squares, results)
            word_squares.pop()

    # Time O(n*N)
    def _build_prefix_hash(self, words: List[str]) -> None:
        self.prefix_hash = defaultdict(list)
        for word in words:
            for i in range(1, self.N):
                prefix = word[:i]
                self.prefix_hash[prefix].append(word)

test_cases = [
    [[["ball","area","lead","lady"],["wall","area","lead","lady"]], ["area","lead","wall","lady","ball"]],
    [[["baba","abat","baba","atal"],["baba","abat","baba","atan"]], ["abat","baba","atan","atal"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.wordSquares(words)
    actual.sort()
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")