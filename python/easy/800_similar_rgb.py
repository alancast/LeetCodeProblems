class Solution:
    # Really confusing and stupid question. Just pasting answer
    # Time O(1)
    # Space O(1)
    def similarRGB(self, color: str) -> str:
        # Given string 'color_section' representing a two-digit
        # base 16 number "AB", find out the number "XX" that
        # has the highest similarity to "AB".
        def findTarget(color_section):
            num = int(color_section, 16)

            # Get the rounded value of num to 17.
            x = round(num / 17)

            # Return "XX", the pattern of the highest similarity.
            return hex(x)[-1] * 2

        # Split input color into three sections, find out the best
        # fit for each section and attach it to 'target_color'.
        target_color = "#"
        for i in range(1, 6, 2):
            target_color += findTarget(color[i:i + 2])

        return target_color

test_cases = [
    ["#11ee66", "#09f166"],
    ["#5544dd", "#4e3fe1"]
]
solution = Solution()
for expected, color in test_cases:
    actual = solution.similarRGB(color)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: color: {color}")

print("Ran all tests")
