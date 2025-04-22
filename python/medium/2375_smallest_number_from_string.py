from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self._validate_input(pattern)
        return self._smallest_number_precomputed_d_length(pattern)
    
    # Time O(n) as we go through the pattern twice
    # Space O(n) as we create result list and d len list each of size n
    def _smallest_number_precomputed_d_length(self, pattern: str) -> str:
        # Precompute how many D's will follow from this index
        ds_in_a_row = [0] * len(pattern)
        num_ds = 0
        for index in range(len(pattern)-1, -1, -1):
            if pattern[index] == 'D':
                num_ds += 1
            else:
                num_ds = 0

            ds_in_a_row[index] = num_ds

        # Build result string in one go
        result = []
        max_so_far = curr_max = 1
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                result.append(str(curr_max))
                curr_max = max_so_far + 1
                max_so_far += 1
            else:
                result.append(str(curr_max + ds_in_a_row[i]))
                max_so_far = max(max_so_far, curr_max + ds_in_a_row[i])

        # Append last_character
        if pattern[-1] == 'D':
            result.append(str(int(result[-1]) - 1))
        else:
            result.append(str(max_so_far))

        return ''.join(result)

    # Time O(n) as we go through the pattern once
    # Space O(n) as we create result list of size n
    def _smallest_number_sliding_window(self, pattern: str) -> str:
        result = []
        previous_index = 0

        # Iterate through the pattern
        # If we see an I just add chars (and reverse any that were previously added that need reversed)
        # If we see a D kick the can down the road til our next I
        for index in range(len(pattern) + 1):
            result.append(str(index + 1))

            # We've reached the end or an I so append final characters (reverse substring when necessary)
            if index == len(pattern) or pattern[index] == 'I':
                result[previous_index:] = reversed(result[previous_index:])
                previous_index = index + 1
           
        return ''.join(result)

    # Time O(n) as we go through the pattern once
    # Space O(n) as the whole pattern could be in the stack
    def _smallest_number_stack(self, pattern: str) -> str:
        result = []
        num_stack = []

        # Iterate through the pattern
        for index in range(len(pattern) + 1):
            # Push the next number onto the stack
            num_stack.append(index + 1)

            # If 'I' is encountered or we reach the end, pop all stack elements
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))     
           
        return ''.join(result)
    
    # Time O(n) as recursion builds the number by going through the pattern once
    # Space O(n) as the call stack and result array are of size n
    def _smallest_number_recursion(self, pattern: str) -> str:
        result = []
        self._build_sequence(0, 0, pattern, result)
        return ''.join(result[::-1])
    
    # Recursively build the sequence
    def _build_sequence(self, current_index: int, current_count: int, pattern: str, result: List[str]) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                # If 'I', increment the count and move to the next index
                self._build_sequence(current_index + 1, current_index + 1, pattern, result)
            else:
                # If 'D', keep the count and move to the next index
                current_count = self._build_sequence(current_index + 1, current_count, pattern, result)

        result.append(str(current_count + 1))

        # Return the next count for the sequence
        return current_count + 1

    # Time O(n*10^n) where n is length of pattern + 1
    # Space O(1)
    def _smallest_number_brute_force(self, pattern: str) -> str:
        n = len(pattern)
        min_num = pow(10, n)
        max_num = pow(10, n+1)

        for i in range(min_num, max_num):
            if self._is_num_is_valid(i, pattern):
                return str(i)

    def _is_num_is_valid(self, num: int, pattern: str) -> bool:
        num_str = str(num)
        # Make sure there are no duplicate chars
        seen = set()
        for char in num_str:
            if char in seen or char == '0':
                return False
            
            seen.add(char)

        # Make sure every rule is followed
        for i, char in enumerate(pattern):
            if char == 'I':
                if num_str[i] > num_str[i+1]:
                    return False
            elif char == 'D':
                if num_str[i] < num_str[i+1]:
                    return False

        return True

    def _validate_input(self, pattern: str) -> None:
        if len(pattern) < 1 or len(pattern) > 8:
            raise ValueError("pattern must be between 1 and 8 characters")
        
        for char in pattern:
            if char != 'D' and char != 'I':
                raise ValueError("pattern must consist of only I and D")
    
test_cases = [
    ["123549876", "IIIDIDDD"],
    ["21", "D"],
    ["12", "I"],
    ["987654321", "DDDDDDDD"],
    ["4321", "DDD"],
    ["214365879", "DIDIDIDI"]
]
solution = Solution()
for expected, pattern in test_cases:
    actual = solution.smallestNumber(pattern)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: pattern: {pattern}")

print("Ran all tests")