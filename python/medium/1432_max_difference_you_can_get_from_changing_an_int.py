class Solution:
    # Actually slower logic than below but easier to read
    # Time O(n) as we go through the full num a few times
    # Space O(n) as we store copies of the num
    def maxDiff(self, num: int) -> int:
        max_num = str(num)
        # Find the first non 9 and replace all it's occurrences with 9
        for digit in max_num:
            if digit != "9":
                max_num = max_num.replace(digit, "9")
                break

        min_num = str(num)
        # Replace the most significant bit with 1
        # Or find a high-order digit that is not equal to the highest digit and replace it with 0.
        for i, digit in enumerate(min_num):
            if i == 0:
                if digit != "1":
                    min_num = min_num.replace(digit, "1")
                    break
            else:
                if digit != "0" and digit != min_num[0]:
                    min_num = min_num.replace(digit, "0")
                    break

        return int(max_num) - int(min_num)

    # N is len of num
    # Time O(n) as we go through the full num once
    # Space O(n) as we store a copy of the num
    def maxDiff_fast(self, num: int) -> int:
        str_num = str(num)
        max_num_arr = []
        max_char = 'z'

        # We don't know whether to replace with 1 or 0, so just do both and find out at end
        min_num_arr_one = []
        min_char_one = 'z'
        min_num_arr_zero = []
        min_char_zero = 'z'

        # Replace the non 9s and non 1s
        first_char = str_num[0]
        for char in str_num:
            # Handle max
            if char == max_char:
                max_num_arr.append('9')
            elif max_char == 'z' and char != '9':
                max_char = char
                max_num_arr.append('9')
            else:
                max_num_arr.append(char)

            # Handle min
            # Replace with one case
            if char == min_char_one:
                min_num_arr_one.append('1')
            elif min_char_one == 'z' and char != '1':
                min_char_one = char
                min_num_arr_one.append('1')
            else:
                min_num_arr_one.append(char)
            # Replace with 0 case
            if char == min_char_zero:
                min_num_arr_zero.append('0')
            # Can't have a leading 0
            elif min_char_zero == 'z' and char != '0' and char != first_char:
                min_char_zero = char
                min_num_arr_zero.append('0')
            else:
                min_num_arr_zero.append(char)

        # Create the ints
        max_int = int(''.join(max_num_arr))

        # Make sure number isn't 0
        min_int_one = int(''.join(min_num_arr_one))
        min_int = int(''.join(min_num_arr_zero))
        if min_int == 0 or min_int_one < min_int:
            min_int = min_int_one

        # Do the math
        return max_int - min_int
    
test_cases = [
    [888, 555],
    [8, 9],
    [820000, 123456]
]
solution = Solution()
for expected, num in test_cases:
    actual = solution.maxDiff(num)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: num: {num}")

print("Ran all tests")