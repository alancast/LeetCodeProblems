class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for portion in path.split("/"):
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str

testCases = [
    ["/home/", "/home"],
    ["/../", "/"],
    ["/../bar", "/bar"],
    ["/home//foo/", "/home/foo"],
    ["/home/foo/../bar", "/home/bar"]
]
implementation = Solution()
for path, expected in testCases:
    answer = implementation.simplifyPath(path)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUT: {path}")