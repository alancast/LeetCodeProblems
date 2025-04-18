class Solution:
    def countAndSay(self, n: int) -> str:
        self.validate_input(n)
        return self.count_and_say_brute_force(n)
    
    # Time O(2^n) as we compute each string and each time it basically doubles in size
    # Space O(2^n) as all we store is the answer string but it doubles in size each time basically
    def count_and_say_brute_force(self, n: int) -> str:
        answer = "1"
        for i in range(1, n):
            answer = self.compute_next_string(answer)

        return answer
    
    def compute_next_string(self, rle_str: str) -> str:
        next_str = []
        prev_char = rle_str[0]
        char_count = 0

        for i in range(len(rle_str)):
            if rle_str[i] == prev_char:
                char_count += 1
                continue

            # Char switches so append count of old one and restart count
            next_str.append(str(char_count))
            next_str.append(prev_char)
            prev_char = rle_str[i]
            char_count = 1

        # Make sure to append last character
        next_str.append(str(char_count))
        next_str.append(prev_char)

        return ''.join(next_str)
    
    def validate_input(self, n: int) -> None:
        if n < 1 or n > 30:
            raise ValueError("n must be between 1 and 30") 
    
testCases = [
    [1, "1"],
    [2, "11"],
    [3, "21"],
    [4, "1211"],
    [5, "111221"]
]
solution = Solution()
for n, expected in testCases:
    answer = solution.countAndSay(n)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input {n}")

print("Ran all tests")