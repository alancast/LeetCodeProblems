from heapq import heappop, heappush


class Solution:
    # Time O(n) as we go through every char and do an O(1 (or 26)) operation on it
    # Space O(n) as we store data for every char
    def clearStars(self, s: str) -> str:
        # List of indexes for each char
        # Every time we see one we append, so latest is always at end of list
        char_indexes = [[] for _ in range(26)]

        str_arr = list(s)
        for index, char in enumerate(str_arr):
            # Append this char to the index list of it
            if char != "*":
                char_indexes[ord(char) - ord("a")].append(index)
            # Found a * so remove lowest char
            else:
                for i in range(26):
                    if char_indexes[i]:
                        # Don't actually remove, but instead just set to "*"
                        # When answer is formed we will just ignore all "*"
                        str_arr[char_indexes[i].pop()] = "*"
                        # Make sure to break out of loop to not remove more
                        break
        
        # Be sure to ignore all * in the answer
        return "".join(c for c in str_arr if c != "*")

    # Keep min queue of letters and each time we see a star pop that
    # And insert char to skip into a set
    # Time O(nlogn) as we go over full string and insert each char into min queue which is logn
    # Space O(n) as we store the min queue
    def clearStars_min_queue(self, s: str) -> str:
        skipped_indexes = set()
        min_queue = []
        answer_str = ""
        for i in range(len(s)):
            char = s[i]

            if char == "*":
                char, index = heappop(min_queue)
                skipped_indexes.add(-index)
                # Also be sure to skip the star
                skipped_indexes.add(i)
            else:
                heappush(min_queue, (char, -i))

        for i in range(len(s)):
            if i not in skipped_indexes:
                answer_str += s[i]

        return answer_str
    
test_cases = [
    ["aab", "aaba*"],
    ["ab", "aaba**"],
    ["abc", "abc"]
]
solution = Solution()
for expected, s in test_cases:
    actual = solution.clearStars(s)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: s: {s}")

print("Ran all tests")