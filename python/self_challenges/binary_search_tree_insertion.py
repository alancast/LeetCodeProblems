class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None  
        self.right = None 
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    # Doesn't do any re-arranging or balancing, just inserting
    # Assumes no duplicate numbers
    def insert(self, val):
        node = self.root
    
        # If tree is empty, create new node as root
        if node is None:
            self.root = Node(val)
            return self.root
        
        # Recursively traverse the tree to find insertion point
        while True:
            if val < node.value:
                # Insert into left subtree if it doesn't exist
                # Otherwise traverse into left subtree
                if node.left is None:
                    node.left = Node(val)
                    return self.root
                    
                node = node.left
            elif val > node.value:
                # Insert into right subtree if it doesn't exist
                # Otherwise traverse into right subtree
                if node.right is None:
                    node.right = Node(val)
                    return self.root
    
                node = node.right
