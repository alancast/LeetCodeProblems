class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # Append increasing digits
        for digit in num:
            # If this digit is less than the top of the stack, remove the top of the stack
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # If we still have digits to remove, remove the last k (in case of all increasing)
        if k > 0:
            numStack = numStack[:-k]
        
        # trim the leading zeros
        return "".join(numStack).lstrip('0') or "0"
    
    # This is the same logic as above, just not as python-y
    def removeKdigitsStack(self, num: str, k: int) -> str:
        num_len = len(num)
        if k >= num_len:
            return "0"

        removedIndexes = set()
        digitsToRemove = k
        stack = []
        # Figure out what to remove
        for i in range(num_len):
            digit = int(num[i])
            if not stack or digit >= stack[-1][0]:
                stack.append([digit, i])
            # this number is less than the previous one, so remove previous and continue checking
            else:
                while digitsToRemove > 0 and stack and digit < stack[-1][0]:
                    removedIndexes.add(stack[-1][1])
                    stack.pop()
                    digitsToRemove -= 1

                stack.append([digit, i])

        # If any remaining digits to remove, do so
        while digitsToRemove > 0:
            removedIndexes.add(stack[-1][1])
            stack.pop()
            digitsToRemove -= 1

        # Create new string with number to return
        answerString = "0"
        for i in range(num_len):
            if i in removedIndexes:
                continue
            char = num[i]
            # Don't add leading 0's
            if answerString == "0":
                if char == "0":
                    continue
                else:
                    answerString = char
            else:
                answerString += char

        return answerString
    
    # Slow implementation that each time looks the length of the string for what to remove
    def removeKdigitsSlow(self, num: str, k: int) -> str:
        num_len = len(num)
        if k >= num_len:
            return "0"

        removedIndexes = set()
        digitsToRemove = k
        # Figure out what to remove
        while digitsToRemove > 0:
            previousDigit = 10
            previousIndex = num_len - 1
            removedIndex = False
            for i in range(num_len):
                if i in removedIndexes:
                    continue

                digit = int(num[i])
                if digit < previousDigit and previousDigit != 10:
                    removedIndexes.add(previousIndex)
                    removedIndex = True
                    break

                previousDigit = digit
                previousIndex = i
            
            # See if number to remove is last one
            if not removedIndex:
                removedIndexes.add(previousIndex)

            digitsToRemove -= 1

        # Create new string with number to return
        answerString = "0"
        for i in range(num_len):
            if i in removedIndexes:
                continue
            char = num[i]
            # Don't add leading 0's
            if answerString == "0":
                if char == "0":
                    continue
                else:
                    answerString = char
            else:
                answerString += char

        return answerString

testCases = [
    ["", 1, "0"],
    ["123", 0, "123"],
    ["123", 1, "12"],
    ["123", 2, "1"],
    ["1003", 1, "3"],
    ["100", 1, "0"],
    ["1432219", 3, "1219"],
    ["10200", 1, "200"],
    ["10", 2, "0"],
    ["1234", 3, "1"],
    ["1234", 5, "0"]
]
implementation = Solution()
for num, k, expected in testCases:
    answer = implementation.removeKdigits(num, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected}, got {answer}. Inputs: {num}, {k}")