from collections import defaultdict
from heapq import nsmallest


class TrieNode:
    def __init__(self):
        self.children = {}
        # Dictionary of full sentence to negative count (negative for min heap)
        self.sentences = defaultdict(int)

# Use a Trie and optimize with a heap
class AutocompleteSystem:
    # Time O(nk) where n is num words and k is average length
    def __init__(self, sentences: list[str], times: list[int]):
        # Create the trie and add all values to it
        self.root = TrieNode()
        for sentence, count in zip(sentences, times, strict=False):
            self.add_to_trie(sentence, count)

        # Set the current sentence and node we are on (for input)
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()

    # Time O(n)
    def input(self, c: str) -> list[str]:
        # If user inputs # then it means we want to add the current sentence to the trie
        # Then reset current sentence to nothing
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []

        # Nothing matches this search so far, so return nothing but update current sentence
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []

        # Update current sentence and return the 3 most common items
        self.curr_node = self.curr_node.children[c]
        items = [(val, key) for key, val in self.curr_node.sentences.items()]

        # Do smallest because we are doing negative count
        answer = nsmallest(3, items)
        return [item[1] for item in answer]

    def add_to_trie(self, sentence: str, count: int) -> None:
        node = self.root

        # Go over all letters and make sure in Trie
        for c in sentence:
            # If this letter isn't in the Trie add it
            if c not in node.children:
                node.children[c] = TrieNode()

            # Go to next node
            node = node.children[c]
            # Negative count for min heap
            node.sentences[sentence] -= count

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
