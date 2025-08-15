class TrieNode:
    name: str
    value: int
    children: dict

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        self.children = {}

class FileSystem:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode("", 0)

    def createPath(self, path: str, value: int) -> bool:
        # Not valid paths
        if path == "" or path == "/":
            return False
        
        folders = path.split('/')
        # Remove the initial empty string
        folders = folders[1:]
        n = len(folders)
        node = self.root

        # Make sure all parents have been created
        # But leave last folder for the final creation
        for i in range(n-1):
            folder = folders[i]
            # This folder doesn't exist
            if folder not in node.children:
                return False
            
            node = node.children[folder]

        # We have now gotten here fully from the parents
        # So make sure this folder doesn't already exist and create it

        new_folder = folders[-1]
        if new_folder in node.children:
            return False
        
        # Create the folder (add it to the children of the parent)
        node.children[new_folder] = TrieNode(new_folder, value)

        # Folder successfully created
        return True

    def get(self, path: str) -> int:
        folders = path.split('/')
        # Remove the initial empty string
        folders = folders[1:]

        # Go down full path and return value or -1 if path ever doesn't work
        node = self.root

        for folder in folders:
            if folder not in node.children:
                return -1
            
            node = node.children[folder]

        # We got through the full path so now return the value of the node
        return node.value
    
# Just store everything in a dictionary
# When creating make sure the parent exists
class FileSystemBasic:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        # Make sure path is valid and doesn't already exist
        if path == "/" or len(path) == 0 or path in self.paths:
            return False
        
        # Make sure the parent path exists ('/' is a valid parent)
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False
        
        # Add new path
        self.paths[path] = value

        return True

    def get(self, path: str) -> int:
        if path not in self.paths:
            return -1

        return self.paths[path]