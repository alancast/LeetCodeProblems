class Solution:
    # Sort by difference between min required and actual
    # Want to do tasks with larger differences first to waste fewest energy
    # Time O(nlogn) for sorting algo then O(n) for going through
    # Space O(logn) for sorting algo
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort by largest difference between min required and actual to smallest
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        # Go over all the tasks and add the energies
        answer = 0
        remain = 0
        for energy_to_complete, start_amount_needed in tasks:
            # If we don't have enough to start the task, add to make sure we do
            if remain <= start_amount_needed:
                answer += start_amount_needed - remain

            # Update remaining value of what we have left after doing the task
            remain = max(start_amount_needed - energy_to_complete, remain - energy_to_complete)

        return answer

test_cases = [
    [8, [[1,2],[2,4],[4,8]]],
    [32, [[1,3],[2,4],[10,11],[10,12],[8,9]]],
    [27, [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]]
]
solution = Solution()
for expected, tasks in test_cases:
    actual = solution.minimumEffort(tasks)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: tasks: {tasks}")

print("Ran all tests")
