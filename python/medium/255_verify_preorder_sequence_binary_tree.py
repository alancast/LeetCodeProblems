from typing import List


class Solution:
    # Use a stack and while it's less than final number it's a left subtree
    # As soon as it's greater, find out where it's right subtree of
    # Update new max_min number to make sure everything after it is greater than
    # Time O(n) as we go over whole array with constant time operations
    # Space O(n) as the whole tree could be in the stack
    def verifyPreorder(self, preorder: List[int]) -> bool:
        max_min = 0
        stack = []
        for num in preorder:
            # This num belonged in a left subtree somewhere
            if num < max_min:
                return False
            
            # This num is a continuation of a left subtree 
            # (or is a right subtree right of root)
            if not stack or num < stack[-1]:
                stack.append(num)
                continue

            # We found a num that is a right subtree of something
            while stack and num > stack[-1]:
                max_min = stack.pop()
            
            stack.append(num)

        return True
    
    # Time O(n)
    # Space O(n) for recursion call stack
    def verifyPreorder_recursive(self, preorder: List[int]) -> bool:
        # I must be a list because it being passed by reference makes it so
        # That when right subtree is called I is moved forward to what should be right
        def helper(i: List[int], min_limit: int, max_limit: int) -> bool:
            # Reached end
            if i[0] == len(preorder):
                return True
            
            root = preorder[i[0]]
            # Root is not within limit bounds, so this subtree is impossible
            if not min_limit < root < max_limit:
                return False

            # Process root so move index forward and make sure it is either
            # A valid left or right subtree after that
            i[0] += 1
            left = helper(i, min_limit, root)
            right = helper(i, root, max_limit)
            return left or right
            
        return helper([0], float('-inf'), float('inf'))
    
test_cases = [
    [False, [1,3,4,2]],
    [True, [5,2,1,3,10,8,7,9,11]],
    [True, [5,2,1,3,6]],
    [False, [5,2,6,1,3]]
]
solution = Solution()
for expected, preorder in test_cases:
    actual = solution.verifyPreorder(preorder)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: preorder: {preorder}")

print("Ran all tests")