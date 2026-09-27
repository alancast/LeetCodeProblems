class Solution:
    # Hash the knowledge and replace
    # Time O(n+m)
    # Space O(n+m)
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)

        answer, start = [], -1
        for index, char in enumerate(s):
            # See if start of bracket
            if char == "(":
                start = index
            # See if end of bracket
            elif char == ")":
                # Append to the string whatever the dictionary value is
                answer.append(d.get(s[start + 1 : index], "?"))
                start = -1
            elif start < 0:
                answer.append(char)

        return "".join(answer)

test_cases = [
    ["bobistwoyearsold", "(name)is(age)yearsold", [["name","bob"],["age","two"]]],
    ["hi?", "hi(name)", [["a","b"]]],
    ["yesyesyesaaa", "(a)(a)(a)aaa", [["a","yes"]]]
]
solution = Solution()
for expected, s, knowledge in test_cases:
    actual = solution.evaluate(s, knowledge)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: s: {s}, knowledge: {knowledge}")

print("Ran all tests")
