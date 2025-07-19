from collections import defaultdict
from typing import List


class Solution:

    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    # Create a Trie
    # Time O(n*L)
    # Space O(n*l)
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Build Trie from all folder paths
        for path in folder:
            current_node = self.root
            folders = path.split("/")

            for folder_name in folders:
                # Skip root level
                if folder_name == "":
                    continue

                # Create new node if it doesn't exist
                if folder_name not in current_node.children:
                    current_node.children[folder_name] = self.TrieNode()
                current_node = current_node.children[folder_name]

            # Mark the end of the folder path
            current_node.is_end_of_folder = True

        # Check each path for subfolders
        answer = []
        for path in folder:
            current_node = self.root
            folders = path.split("/")
            is_subfolder = False

            for i, folder_name in enumerate(folders):
                # Skip root level
                if folder_name == "":
                    continue

                next_node = current_node.children[folder_name]
                # Check if the current folder path is a subfolder of an existing folder
                # Found a subfolder so break out
                # Make sure the is_end_of_folder isn't referring to this folder
                if next_node.is_end_of_folder and i != len(folders) - 1:
                    is_subfolder = True
                    break
    
                current_node = next_node

            # If not a subfolder after getting to end, add to the answer
            if not is_subfolder:
                answer.append(path)

        return answer
    
    # Sort folders list (so subfolders guaranteed to appear after folder)
    # Time O(n*Llogn) for sorting
    # Space O(n*l) for sorting bu also for creating answer set
    def removeSubfolders_sorting(self, folder: List[str]) -> List[str]:
        # Sort the folders alphabetically
        folder.sort()

        answer = [folder[0]]

        # Iterate through each folder and check if it's a sub-folder of the last added folder in the answer
        for i in range(1, len(folder)):
            last_folder = answer[-1]
            last_folder += "/"

            # Check if the current folder starts with the last added folder path
            if not folder[i].startswith(last_folder):
                answer.append(folder[i])

        return answer
    
test_cases = [
    [["/a","/c/d","/c/f"], ["/a","/a/b","/c/d","/c/d/e","/c/f"]],
    [["/a","/c"], ["/a","/a/b","/c/d/e","/c/d/f","/c"]],
    [["/a"], ["/a","/a/b/c","/a/b/d"]],
    [["/a/b/c","/a/b/ca","/a/b/d"], ["/a/b/c","/a/b/ca","/a/b/d"]]
]
solution = Solution()
for expected, folder in test_cases:
    actual = solution.removeSubfolders(folder)
    if set(expected) != set(actual):
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: folder: {folder}")

print("Ran all tests")