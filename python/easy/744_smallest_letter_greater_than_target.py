class Solution:
    # Since letters is sorted can do binary search
    # Time O(logn)
    # Space O(1)
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        # Do binary search
        while left <= right:
            mid = (left + right) // 2
            # Need a greater letter
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # Then all letters were smaller than target
        if left == len(letters):
            return letters[0]

        return letters[left]

    # Just go over the letters once and find smallest greater than target
    # Time O(n)
    # Space O(1)
    def nextGreatestLetter_brute(self, letters: list[str], target: str) -> str:
        # Just a placeholder for after z
        answer = "{"

        for letter in letters:
            if letter > target and letter < answer:
                answer = letter

        # Make sure we found one greater than target
        if answer == "{":
            return letters[0]

        return answer

test_cases = [
    ["c", ["c", "f", "j"], "a"],
    ["f", ["c","f","j"], "c"],
    ["x", ["x","x","y","y"], "z"]
]
solution = Solution()
for expected, letters, target in test_cases:
    actual = solution.nextGreatestLetter(letters, target)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: letters: {letters}, target: {target}")

print("Ran all tests")
