from typing import List


class Solution:
    # Time O(mlogn+nlogm)
    # Space O(1)
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Do binary search to find column with min_x and max_x
        # And for row of min_y, max_y
        min_x = max_x = x
        min_y = max_y = y
        n_x = len(image)
        n_y = len(image[0])

        # find min_x
        left = 0
        right = x
        while left <= right:
            found_one = False
            mid = (left + right) // 2
            for i in range(n_y):
                if image[mid][i] == "1":
                    right = mid - 1
                    found_one = True
                    min_x = mid
                    break
            
            if not found_one:
                left = mid + 1
        
        # find max_x
        left = x
        right = n_x - 1
        while left <= right:
            found_one = False
            mid = (left + right) // 2
            for i in range(n_y):
                if image[mid][i] == "1":
                    left = mid + 1
                    found_one = True
                    max_x = mid
                    break
            
            if not found_one:
                right = mid - 1
        
        # find min_y
        left = 0
        right = y
        while left <= right:
            found_one = False
            mid = (left + right) // 2
            for i in range(n_x):
                if image[i][mid] == "1":
                    right = mid - 1
                    found_one = True
                    min_y = mid
                    break
            
            if not found_one:
                left = mid + 1
        
        # find max_y
        left = y
        right = n_y - 1
        while left <= right:
            found_one = False
            mid = (left + right) // 2
            for i in range(n_x):
                if image[i][mid] == "1":
                    left = mid + 1
                    found_one = True
                    max_y = mid
                    break
            
            if not found_one:
                right = mid - 1
            
        return (max_x - min_x + 1) * (max_y - min_y + 1)

    # Time O(k) where k is number of 1's (guaranteed to be <= m x n)
    # Space O(k) as queue could include all k neighbors at once
    def minArea_bfs(self, image: List[List[str]], x: int, y: int) -> int:
        # Append to queue every touching 1
        # Update grid to be 0 at that location
        # Keep track of min and max x and y
        min_x = max_x = x
        min_y = max_y = y
        n_x = len(image)
        n_y = len(image[0])

        queue = [(x,y)]
        image[x][y] = "0"
        while queue:
            x, y = queue.pop()
            # check neighbors
            if x-1 >= 0 and image[x-1][y] == "1":
                queue.append((x-1, y))
                image[x-1][y] = "0"
            if x+1 < n_x and image[x+1][y] == "1":
                queue.append((x+1, y))
                image[x+1][y] = "0"
            if y-1 >= 0 and image[x][y-1] == "1":
                queue.append((x, y-1))
                image[x][y-1] = "0"
            if y+1 < n_y and image[x][y+1] == "1":
                queue.append((x, y+1))
                image[x][y+1] = "0"
            
            # update min and maxes
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
    
        return (max_x - min_x + 1) * (max_y - min_y + 1)
    
test_cases = [
    [6, [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], 0, 2]
]
solution = Solution()
for expected, image, x, y in test_cases:
    actual = solution.minArea(image, x, y)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: image: {image}, x: {x}, y: {y}")

print("Ran all tests")