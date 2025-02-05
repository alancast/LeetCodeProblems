class Solution:
    # Pure math solution, proof is on leet code page
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    # This is the intuitive solution that comes to mind
    # Turns out there is just a pure math solution that is O(1) above
    def addDigitsRecurse(self, num: int) -> int:
        if num < 10:
            return num
        
        tempNum = 0
        while num > 0:
            tempNum = tempNum + (num % 10)
            num = num // 10
        
        return self.addDigitsRecurse(tempNum)

testCases = [
    [38, 2],
    [0, 0],
    [12, 3]
]
solution = Solution()
for num, expected in testCases:
    answer = solution.addDigits(num)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Input {num}")