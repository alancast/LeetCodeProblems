class Solution:
    # Less fun mathy way to do it that is still O(n) and O(1)
    # Faster due to python optimizations, but should be same
    # Remove cars on edges, then every car left will collide
    # Time O(n)
    # Space O(1)
    def countCollisions(self, directions: str) -> int:
        dirs = directions.lstrip("L").rstrip("R")
        return len(dirs) - dirs.count("S")

    # Go over string once and keep track of cars and collisions
    # Time O(n)
    # Space O(1)
    def countCollisions_fun(self, directions: str) -> int:
        answer = 0

        cars_going_right = 0
        stopped_car_to_left = False
        for char in directions:
            # Car going left
            if char == 'L':
                # Will hit first car going right then be still
                if cars_going_right > 0:
                    answer += cars_going_right + 1
                    stopped_car_to_left = True
                # This car will eventually hit the collision
                elif stopped_car_to_left == True:
                    answer += 1
                
                # Make sure there are no more cars going right
                cars_going_right = 0
            # Car staying put will only be hit by cars going right
            elif char == 'S':
                # All accidents will be stationary
                if cars_going_right > 0:
                    answer += cars_going_right
                
                cars_going_right = 0
                stopped_car_to_left = True
            # Car is going right
            elif char == 'R':
                cars_going_right += 1
                stopped_car_to_left = False

        return answer

test_cases = [
    [5, "RLRSLL"],
    [0, "LLRR"]
]
solution = Solution()
for expected, directions in test_cases:
    actual = solution.countCollisions(directions)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: directions: {directions}")

print("Ran all tests")
