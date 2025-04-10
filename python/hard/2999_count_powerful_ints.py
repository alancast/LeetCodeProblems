class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        self.validate_inputs(start, finish, limit, s)

        # Subtract 1 from start because range in problem is inclusive
        start_str = str(start - 1)
        finish_str = str(finish)

        return self.calculate(finish_str, s, limit) - self.calculate(start_str, s, limit)

    def calculate(self, num: str, s: str, limit: int) -> int:
        # If num is less than the suffix or same length as suffix answer is simple
        if len(num) < len(s):
            return 0
        if len(num) == len(s):
            return 1 if num >= s else 0

        suffix = num[len(num) - len(s):]
        count = 0
        pre_len = len(num) - len(s)

        # Count the possible prefixes
        for i in range(pre_len):
            # Number is above limit so do power of limit ^ 10s
            if limit < int(num[i]):
                count += pow((limit + 1), (pre_len - i))
                return count
            # Number is below limit so they are all possible 
            count += int(num[i]) * pow((limit + 1), (pre_len - 1 - i))

        # See if we need to add final one for suffix
        if suffix >= s:
            count += 1

        return count
    
    def validate_inputs(self, start: int, finish: int, limit: int, s: str) -> None:
        if start > finish:
            raise ValueError("Start can't be more than finish")
        if start < 1 or finish < 1:
            raise ValueError("Start and Finish must both be positive")
        if limit < 1 or limit > 9:
            raise ValueError("limit must be between 1 and 9")
        for char in s:
            if int(char) > limit:
                raise ValueError("Every digit in s must be less than limit")
    
test_cases = [
    [8, 20, 1159, 5, "20"],
    [7, 1, 771, 7, "72"],
    [8, 1, 771, 7, "70"],
    [9, 1, 971, 9, "72"],
    [90, 1, 9071, 9, "72"],
    [10, 1, 971, 9, "70"],
    [91, 1, 9071, 9, "70"],
    [5, 1, 6000, 4, "124"],
    [25, 1, 60000, 4, "124"],
    [2, 15, 215, 6, "10"],
    [4, 1000, 5000, 6, "300"],
    [5, 100, 5000, 6, "300"],
    [0, 1000, 2000, 4, "3000"],
    [1, 1000, 2000, 4, "1400"]
]
solution = Solution()
for expected, start, finish, limit, s in test_cases:
    actual = solution.numberOfPowerfulInt(start, finish, limit, s)
    if actual != expected:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: start: {start}, finish: {finish}, limit: {limit}, s: {s}")

print("Ran all tests")