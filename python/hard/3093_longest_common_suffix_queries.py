class TrieNode:
    min_len: int
    min_len_index: int
    children: dict

    def __init__(self):
        self.children = {}
        # Just a default max len
        self.min_len = 100000000


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str, index: int) -> None:
        n = len(word)
        node = self.root

        # Set the root value min
        if n < node.min_len:
            node.min_len = n
            node.min_len_index = index

        # Go over each char and add the word to the trie
        for i in range(n-1, -1, -1):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

            # See if we have a new min len
            if n < node.min_len:
                node.min_len = n
                node.min_len_index = index

    def findIndex(self, word: str) -> int:
        n = len(word)
        node = self.root

        # Go over each char and add the word to the trie
        for i in range(n-1, -1, -1):
            char = word[i]
            # If this char isn't there we no longer have a shared suffix
            # So break out and return whatever this nodes shortest index is
            if char not in node.children:
                break

            node = node.children[char]

        return node.min_len_index

class Solution:
    # Build a Trie from backwards. In each node also store dist to end
    # Time O(nd + qd) where d is length of the word or query, n is num words, q is num queries
    # Space O(nd)
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        # Build the trie
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.addWord(word, i)

        # Now go over the queries and build answer
        answer = []
        for word in wordsQuery:
            answer.append(trie.findIndex(word))

        return answer

test_cases = [
    [[1,1,1], ["abcd","bcd","xbcd"], ["cd","bcd","xyz"]],
    [[2,0,2], ["abcdefgh","poiuygh","ghghgh"], ["gh","acbfgh","acbfegh"]]
]
solution = Solution()
for expected, words_container, words_query in test_cases:
    actual = solution.stringIndices(words_container, words_query)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: words_container: {words_container}, words_query: {words_query}")

print("Ran all tests")
