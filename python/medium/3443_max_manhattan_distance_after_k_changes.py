class Solution:
    # Go over string once, count all N,E,S,W
    # Modify less frequent of E/W and N/S
    # Each modification increases manhattan distance by 2
    # If k < num modifications then take max manhattan distance + k*2
    # If K > num modifications then length of string is manhattan distance
    # Because every time we move we go further away in some direction
    # Time O(n) as we go over string once
    # Space O(1)
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)

        latitude = longitude = answer = 0
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1

            answer = max(answer, min(abs(latitude) + abs(longitude) + (k * 2), i + 1))

        return answer
    
test_cases = [
    [3, "NWSE", 1],
    [4, "ENNSW", 1],
    [3, "EWEWEWNS", 1],
    [3, "NSEWEWEW", 1],
    [3, "NWE", 1],
    [6, "NSWWEW", 3]
]
solution = Solution()
for expected, s, k in test_cases:
    actual = solution.maxDistance(s, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, k: {k}")

print("Ran all tests")