from typing import List


class Solution:
    # Backtracking solution.
    # Pick 2 numbers, do an operation on them, add new number to array
    # Do that until array is size 1, then see if number is 24 or not
    # If not, backtrack and try with a different operation
    # End if all operations with all numbers tried (or found one that's true)
    # Time O(N!) can be more precise with more math
    # Space O(N^2) recursive stack and each one having array of len cards
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.check_if_result_reached(cards)

    # Returns a list of all possible operations we can perform on two numbers.
    def generate_possible_results(self, a: float, b: float) -> List[float]:
        # Ones that we can definitely do
        res = [a + b, a - b, b - a, a * b]

        # Make sure we don't divide by 0
        if a:
            res.append(b / a)
        if b:
            res.append(a / b)

        return res
    
    # Check if using current list we can reach result 24.
    def check_if_result_reached(self, cards: List[float]) -> bool:
        # Base Case: We have only one number left, check if it is approximately 24.
        # Approximately because floating point rounding could be slightly off
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.1

        # Wasn't equal to 24, so go over all cards and try
        for i in range(len(cards)):
            card_i = cards[i]

            for j in range(i + 1, len(cards)):
                card_j = cards[j]

                # Create a new list with the remaining numbers and the new result.
                # So just remove cards[i] and cards[j]
                new_list = [number for k, number in enumerate(cards) if (k != i and k != j)]
                
                # Generate all possible operations between these two numbers
                # Try them all iteratively and add result then see if we can reach 24
                for res in self.generate_possible_results(card_i, card_j):
                    # Add the new result to the list.
                    new_list.append(res)
                    
                    # Check if using this new list we can obtain the result 24.
                    if self.check_if_result_reached(new_list):
                        return True
                    
                    # Backtrack: remove the result from the list.
                    new_list.pop()

        # Tried all combinations and none worked, so can't be done
        return False
    
test_cases = [
    [True, [4,1,8,7]],
    [False, [1,2,1,2]]
]
solution = Solution()
for expected, cards in test_cases:
    actual = solution.judgePoint24(cards)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: cards: {cards}")

print("Ran all tests")