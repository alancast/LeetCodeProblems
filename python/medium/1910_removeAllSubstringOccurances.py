from typing import List

class Solution:
    def remove_occurrences(self, s: str, part: str) -> str:
        return self.__remove_occurrences_kmp(s, part)
    
    # Time O(n^2) Space O(1) (potentially O(n) if copy string)
    def __remove_occurrences_basic(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "")
        return s
    
    # Time O(nm) Space O(n+m) m is size of part
    def __remove_occurrences_stack(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= len(part) and self.__check_match(stack, part):
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)
    
    def __check_match(self, stack: list, part: str) -> bool:
        part_len = len(part)
        stack_len = len(stack)
        for i in range(part_len):
            if stack[stack_len - part_len + i] != part[i]:
                return False

        return True
    
    # Time O(n + m) Space O(n + m) m is size of part
    def __remove_occurrences_kmp(self, s: str, part: str) -> str:
        lps_array = self.__compute_lps_array(part)
        char_stack = []
        pattern_indexes = [0] * len(s)
        pattern_index = 0
        index = 0
        
        s = list(s)
        part = list(part)
        while index < len(s):
            char = s[index]
            char_stack.append(char)
            # Pattern matching continues
            if char == part[pattern_index]:
                pattern_index += 1
                pattern_indexes[len(char_stack) - 1] = pattern_index

                # full part match, so pop them all
                if pattern_index == len(part):
                    for _ in range(len(part)):
                        char_stack.pop()
                    
                    if len(char_stack) == 0:
                        pattern_index = 0
                    else:
                        pattern_index = pattern_indexes[len(char_stack) - 1]
            # Pattern matching broke
            else:
                if pattern_index != 0:
                    pattern_index = lps_array[pattern_index - 1]
                    char_stack.pop()
                    index -= 1
                else:
                    pattern_indexes[len(char_stack) - 1] = 0
            
            index += 1

        return "".join(char_stack)
    
    def __compute_lps_array(self, pattern: str) -> List[int]:
        lps_array = [0] * len(pattern)
        prefix_length = 0
        for index in range(1, len(pattern)):
            if pattern[index] == pattern[prefix_length]:
                prefix_length += 1
            else:
                while prefix_length != 0 and pattern[index] != pattern[prefix_length]:
                    prefix_length = lps_array[prefix_length - 1]
                
                if pattern[index] == pattern[prefix_length]:
                    prefix_length += 1

            lps_array[index] = prefix_length
        
        return lps_array

test_cases = [
    ["ababc", "abab", "c"],
    ["daabcbaabcbc", "abc", "dab"],
    ["axxxxyyyyb", "xy", "ab"],
    ["aabbaabb", "ab", ""],
    ["hello", "ll", "heo"],
    ["mississippi", "iss", "mippi"]
]
solution = Solution()
for s, part, expected in test_cases:
    answer = solution.remove_occurrences(s, part)
    if answer != expected:
        print(f"FAILED TEST: expected {expected} but got {answer}. Inputs: s: {s} part: {part}")

print("Ran all tests")