class TrieNode:
    children: list

    def __init__(self):
        # Each node has up to 10 possible children (digits 0-9)
        self.children = [None] * 10


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    # Insert a number into the Trie by treating it as a string of digits
    def insert(self, num: int) -> None:
        node = self.root

        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            # If the current node doesn't have any children of this digit, add new one
            if not node.children[idx]:
                node.children[idx] = TrieNode()

            # Set node to the child
            node = node.children[idx]

    # Find the longest common prefix for a number in arr2 with the Trie
    def find_longest_prefix(self, num: int) -> int:
        node = self.root
        num_str = str(num)
        len = 0

        # Go over the num and if there are still kids keep going
        for digit in num_str:
            idx = int(digit)
            # Increase length if the current digit matches
            if node.children[idx]:
                len += 1
                node = node.children[idx]
            # Stop if no match for the current digit
            else:
                break

        return len

class Solution:
    # Create a Trie of every element in the first arr
    # Then go through second and add to trie and store longest
    # Time O(n*d + m*d)
    # Space O(n*d)
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = Trie()

        # Step 1: Insert all numbers from arr1 into the Trie
        for num in arr1:
            trie.insert(num)

        longest_prefix = 0
        # Step 2: Find the longest prefix match for each number in arr2
        for num in arr2:
            len = trie.find_longest_prefix(num)
            longest_prefix = max(longest_prefix, len)

        return longest_prefix

test_cases = [
    [3, [1,10,100], [1000]],
    [0, [1,2,3], [4,4,4]]
]
solution = Solution()
for expected, arr1, arr2 in test_cases:
    actual = solution.longestCommonPrefix(arr1, arr2)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: arr1: {arr1}, arr2: {arr2}")

print("Ran all tests")
