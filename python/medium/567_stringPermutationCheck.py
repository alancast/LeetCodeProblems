from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1_arr = [0] * 26
        sliding_arr = [0] * 26
        for i in range(s1_len):
            char1 = s1[i]
            char2 = s2[i]
            s1_arr[ord(char1) - ord('a')] += 1
            sliding_arr[ord(char2) - ord('a')] += 1
        
        count = 0
        for i in range(26):
            if s1_arr[i] == sliding_arr[i]:
                count += 1
                
        for i in range(s1_len, s2_len):
            leaving_index = ord(s2[i-s1_len]) - ord('a')
            adding_index = ord(s2[i]) - ord('a')
            if count == 26:
                return True

            sliding_arr[adding_index] += 1
            if sliding_arr[adding_index] == s1_arr[adding_index]:
                count += 1
            elif sliding_arr[adding_index] == s1_arr[adding_index] + 1:
                count -= 1

            sliding_arr[leaving_index] -= 1
            if sliding_arr[leaving_index] == s1_arr[leaving_index]:
                count += 1
            elif sliding_arr[leaving_index] == s1_arr[leaving_index] - 1:
                count -= 1

        return count == 26

    def checkInclusionArr(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1_arr = [0] * 26
        sliding_arr = [0] * 26
        for i in range(s1_len):
            char1 = s1[i]
            char2 = s2[i]
            s1_arr[ord(char1) - ord('a')] += 1
            sliding_arr[ord(char2) - ord('a')] += 1
        
        if sliding_arr == s1_arr:
            return True

        for i in range(s1_len, s2_len):
            char_leaving = s2[i-s1_len]
            char_adding = s2[i]
            sliding_arr[ord(char_leaving) - ord('a')] -= 1
            sliding_arr[ord(char_adding) - ord('a')] += 1
        
            if sliding_arr == s1_arr:
                return True

        return False

    def checkInclusionHash(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1_counter = Counter(s1)
        sliding_counter = Counter(s2[:s1_len])
        if s1_counter == sliding_counter:
            return True

        for i in range(s1_len, s2_len):
            sliding_counter[s2[i-s1_len]] -= 1
            if sliding_counter[s2[i-s1_len]] == 0:
                del sliding_counter[s2[i-s1_len]]
            sliding_counter[s2[i]] = sliding_counter.get(s2[i], 0) + 1
            if s1_counter == sliding_counter:
                return True

        return False

testCases = [
    ["ab", "eidbaooo", True],
    ["a", "a", True],
    ["ab", "abc", True],
    ["abc", "ab", False],
    ["a", "b", False],
    ["ab", "eidboaoo", False]
]
solution = Solution()
for s1, s2, expected in testCases:
    answer = solution.checkInclusion(s1, s2)
    if answer != expected:
        print(f"FAILED TEST: Inputs: {s1}, {s2}, got {answer}")