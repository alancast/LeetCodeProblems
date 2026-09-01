class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    # Insert a word into the trie
    def _insert(self, word):
        node = self.root

        # Add every char to the trie
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]

        # Make sure end of word is marked as such
        node.is_end_of_word = True

    # Check if all prefixes of the word exist in the trie
    def _has_all_prefixes(self, word):
        node = self.root

        # Make sure every char in word is end of a different word
        for char in word:
            # If this char isn't the end of the word we are missing a prefix
            if char not in node.children or not node.children[char].is_end_of_word:
                return False
            node = node.children[char]

        # All chars are end of a word so all prefixes exist
        return True


class Solution:
    # Build a Trie. And then go over all words and make sure all prefixes are words as well
    # Time O(n*l) where n is the number of words and l is the length of the longest word
    # Space O(n*l) for the trie
    def longestWord(self, words: list[str]) -> str:
        trie = Trie()
        answer = ""

        # Insert all words into the trie
        for word in words:
            trie._insert(word)

        # Check each word and update the longest valid word
        for word in words:
            # See if we should check for prefixes (if this word is longer)
            is_better_length = (
                len(word) > len(answer)
                or (
                    len(word) == len(answer)
                    and word < answer
                )
            )

            # If the word is longer see if all prefixes exist and if so update the answer
            if is_better_length and trie._has_all_prefixes(word):
                answer = word

        return answer

test_cases = [
    ["kiran", ["k","ki","kir","kira", "kiran"]],
    ["apple", ["a","banana","app","appl","ap","apply","apple"]],
    ["", ["abc", "bc", "ab", "qwe"]]
]
solution = Solution()
for expected, words in test_cases:
    actual = solution.longestWord(words)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: words: {words}")

print("Ran all tests")
