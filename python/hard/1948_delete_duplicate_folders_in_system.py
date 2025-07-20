from collections import Counter
from typing import List


class Trie:
    # current node structure's serialized representation
    serial: str = ""
    # current node's child nodes
    children: dict

    def __init__(self):
        self.children = {}


class Solution:
    # Build tree of paths, then serialize subnodes of all nodes
    # Then look for dupes and delete
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        # Build tree of paths
        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        # Construct all serializations and insert into hash map
        self.freq = Counter()
        self._construct(root)

        self.answer = []
        # record the path from the root node to the current node.
        self.path = []
        self._operate(root)

        return self.answer
    
    # Construct serialization of node
    # post-order traversal based on depth-first search
    # calculate the serialized representation of each node structure
    def _construct(self, node: Trie) -> None:
        # if it is a leaf node, then the serialization is represented 
        # as an empty string, and no operation is required.
        if not node.children:
            return

        v = []
        # if it is not a leaf node, the serialization representation 
        # of the child node structure needs to be calculated first.
        for folder, child in node.children.items():
            self._construct(child)
            v.append(folder + "(" + child.serial + ")")

        # to prevent issues with serialization order, sorting is needed
        v.sort()
        node.serial = "".join(v)

        # Add serialization to counter for duplicate counting
        self.freq[node.serial] += 1

    # Go over all the nodes and see if there are duplicate folders
    def _operate(self, node: Trie) -> None:
        # if the serialization appears more than once in the hash table, 
        # it needs to be deleted.
        if self.freq[node.serial] > 1:
            return
        
        # Serialization is unique so add this path to the answer set
        if self.path:
            self.answer.append(self.path[:])

        # Go over all it's children and repeat the process
        for folder, child in node.children.items():
            self.path.append(folder)
            self._operate(child)
            self.path.pop()

test_cases = [
    [[["d"],["d","a"]], [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]],
    [[["c"],["c","b"],["a"],["a","b"]], [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]],
    [[["c"],["c","d"],["a"],["a","b"]], [["a","b"],["c","d"],["c"],["a"]]]
]
solution = Solution()
for expected, paths in test_cases:
    actual = solution.deleteDuplicateFolder(paths)
    expected.sort()
    actual.sort()
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: paths: {paths}")

print("Ran all tests")