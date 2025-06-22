from typing import List


class Solution:
    # Same logic as below but more python-y
    # Time O(n) as we go through the full string once and do O(1) operations
    # Space O(1) as all that we create is used for the return
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        answer = []

        index = 0
        # Append all k sized chunks from string
        while index < n:
            answer.append(s[index : index + k])
            index += k

        # Fill last answer with however many filler chars are needed
        answer[-1] += fill * (k - len(answer[-1]))

        return answer

    # Time O(n) as we go through the full string once and do O(1) operations
    # Space O(1) as all that we create is used for the return
    def divideString_less_python(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        index = 0

        answer = []
        # Just subtracting k to remove an if check for out of bounds (speeds up runtime)
        while index <= n - k:
            temp_arr = [fill] * k
            for i in range(k):
                temp_arr[i] = s[index]
                index += 1
            
            answer.append(''.join(temp_arr))

        # Append the last chars
        while index < n:
            temp_arr = [fill] * k
            for i in range(k):
                if index >= n:
                    break

                temp_arr[i] = s[index]
                index += 1
            
            answer.append(''.join(temp_arr))

        return answer
    
test_cases = [
    [["abc","def","ghi"], "abcdefghi", 3, "x"],
    [["abc","def","ghi", "jxx"], "abcdefghij", 3, "x"],
    [["aax"], "aa", 3, "x"]
]
solution = Solution()
for expected, s, k, fill in test_cases:
    actual = solution.divideString(s, k, fill)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}, fill: {fill}")

print("Ran all tests")