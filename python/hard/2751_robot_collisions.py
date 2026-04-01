class Solution:
    # Sort robots by position then simulate collisions
    # Use a stack to simulate collisions
    # Put right moving robots on stack, and when we encounter left, pop stack until done
    # Time O(nlogn) for sort
    # Space O(n) for sort
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        indices = list(range(n))
        stack = []

        # Sort indices based on their positions
        indices.sort(key=lambda x: positions[x])

        # Go over all robots from left to right, and assess their end state
        for current_index in indices:
            # Add right-moving robots to the stack
            if directions[current_index] == "R":
                stack.append(current_index)
                continue

            # Left moving robot, lets see if it survives and who it takes out
            # If empty stack it survives moving left for the rest of it's happy fun life
            while stack and healths[current_index] > 0:
                # Pop the top robot from the stack for collision check
                # The top is the one it will collide with first
                top_index = stack.pop()

                # Top robot survives, current robot is destroyed
                if healths[top_index] > healths[current_index]:
                    healths[top_index] -= 1
                    healths[current_index] = 0
                    stack.append(top_index)
                # Current robot survives, top robot is destroyed
                elif healths[top_index] < healths[current_index]:
                    healths[current_index] -= 1
                    healths[top_index] = 0
                # Both robots are destroyed
                else:
                    healths[current_index] = 0
                    healths[top_index] = 0

        # Collect surviving robots and build answer
        answer = []
        for index in range(n):
            if healths[index] > 0:
                answer.append(healths[index])

        return answer

test_cases = [
    [[2,17,9,15,10], [5,4,3,2,1], [2,17,9,15,10], "RRRRR"],
    [[14], [3,5,2,6], [10,10,15,12], "RLRL"],
    [[], [1,2,5,6], [10,10,11,11], "RLRL"]
]
solution = Solution()
for expected, positions, healths, directions in test_cases:
    actual = solution.survivedRobotsHealths(positions, healths, directions)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: positions: {positions}, healths: {healths}, directions: {directions}")

print("Ran all tests")
