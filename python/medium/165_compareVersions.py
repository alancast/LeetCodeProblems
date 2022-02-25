from typing import List


class Solution:
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        # if pointer is set to the end of string return 0
        if p > n - 1:
            return 0, p
        
        # find the end of chunk
        p_end = p + 1
        while p_end < n and version[p_end] != '.':
            p_end += 1

        # retrieve the chunk
        i = int(version[p:p_end]) if p_end != n else int(version[p:n])
        
        return i, p_end + 1
        
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0

    def compareVersionTwoPass(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v1_size = len(v1)
        v2 = version2.split('.')
        v2_size = len(v2)
        i = 0

        while i < v1_size and i < v2_size:
            v1_int = int(v1[i])
            v2_int = int(v2[i])
            if v1_int > v2_int:
                return 1
            elif v2_int > v1_int:
                return -1
            
            i += 1
        
        # Means v2 ended early
        while i < v1_size:
            v1_int = int(v1[i])
            if v1_int > 0:
                return 1
            
            i += 1
        
        # Means v2 ended early
        while i < v2_size:
            v2_int = int(v2[i])
            if v2_int > 0:
                return -1
            
            i += 1

        return 0

testCases = [
    ["1.0", "1.0.0", 0],
    ["1.01", "1.001", 0],
    ["1.1", "1.0", 1],
    ["1.0", "1.1", -1],
    ["0", "0.2", -1],
    ["2.1", "1.2", 1],
]
implementation = Solution()
for version1, version2, expected in testCases:
    answer = implementation.compareVersion(version1, version2)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. Version1: {version1} Version2: {version2}")