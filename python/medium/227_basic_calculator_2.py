from typing import List


class Solution:
    # This time don't use the stack. More space optimized
    # Time O(n)
    # Space O(1)
    def calculate(self, s: str) -> int:
        # Remove whitespace
        s = s.replace(' ', '')

        current_num = last_number = result = 0
        operator = '+'

        # Do all multiplication and division
        n = len(s)
        for i in range(n):
            char = s[i]

            if char.isdigit():
                current_num *= 10
                current_num += int(char)

            # If an operator or last num do the math
            if char in '+-*/' or i == n-1:
                if operator == '+':
                    result += last_number
                    last_number = current_num
                elif operator == '-':
                    result += last_number
                    last_number = -current_num
                elif operator == '*':
                    last_number = last_number * current_num
                else:
                    # Have to do int conversion to handle negative nums without rounding down
                    # e.g. -3//2 is -2 but we want -1
                    last_number = int(last_number / current_num)
                
                # Reset current number
                current_num = 0
                operator = char

        result += last_number
        return result
    
    # Time O(n)
    # Space O(n)
    def calculate_using_stack(self, s: str) -> int:
        # Remove whitespace
        s = s.replace(' ', '')

        stack = []
        current_num = 0
        prev_operator = '+'

        # Do all multiplication and division
        n = len(s)
        for i in range(n):
            char = s[i]

            # If an operator do the math
            if char in '+-*/':
                # Do previous operator if multiplication or div
                self._handle_operation(stack, prev_operator, current_num)
                
                # Reset current number
                current_num = 0
                prev_operator = char
            else:
                current_num *= 10
                current_num += int(char)

            # Handle last char
            if i == n-1:
                self._handle_operation(stack, prev_operator, current_num)

        return sum(stack)

    def _handle_operation(self, stack: List[int], previous_operator: str, current_num: int) -> None:
        # Do previous operator if multiplication or div
        if previous_operator == '*':
            prev_num = stack.pop()
            stack.append(current_num * prev_num)
        elif previous_operator == '/':
            prev_num = stack.pop()
            # Have to do int conversion to handle negative nums without rounding down
            # e.g. -3//2 is -2 but we want -1
            stack.append(int(prev_num / current_num))
        elif previous_operator == '+':
            stack.append(current_num)
        else:
            stack.append(-current_num)


testCases = [
    [13, "14-3/2"],
    [12, "3*2*2"],
    [7, "3+2*2"],
    [1, "3/2"],
    [5, " 3+5 / 2 "]
]
solution = Solution()
for expected, s in testCases:
    answer = solution.calculate(s)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {s}")

print("Ran all tests")