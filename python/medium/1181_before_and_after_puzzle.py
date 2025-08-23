from collections import defaultdict
from typing import List


class Solution:
    # Keep hash map of final word to phrase as well as map of first word to phrase
    # Time O(nlogn) as we sort the answer at the very end
    # Space O(n) as we store hash maps as well as need it for sort
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        first_to_rest = defaultdict(list)
        last_to_rest = defaultdict(list)

        answer = set()
        for phrase in phrases:
            words = phrase.split(' ')

            # See if new connecting phrases can be added
            # See if can be the start of a new phrase
            for ending_phrase in first_to_rest[words[-1]]:
                # Add this phrase
                new_str = ' '.join(words[:-1])

                # Make sure it's not just the solo word before adding starting space
                if new_str:
                    new_str += ' '

                # Add the connecting word
                new_str += words[-1]

                # Add a space if the ending phrase is not empty
                if ending_phrase:
                    new_str += ' '

                # Add the other phrase
                new_str += ending_phrase
                answer.add(new_str)

            # See if it can be the end of a new phrase
            for starting_phrase in last_to_rest[words[0]]:
                # Add starting phrase
                new_str = starting_phrase

                # Make sure it's not just the solo word before adding starting space
                if new_str:
                    new_str += ' '

                # Add the connecting word
                new_str += words[0]

                # Add a space if the ending phrase is not empty
                ending_phrase = ' '.join(words[1:])
                if ending_phrase:
                    new_str += ' '

                # Add the other phrase
                new_str += ending_phrase
                answer.add(new_str)

            # Add these phrases to the maps for future strings
            first_to_rest[words[0]].append(' '.join(words[1:]))
            last_to_rest[words[-1]].append(' '.join(words[:-1]))
    
        return sorted(list(answer))
    
test_cases = [
    [["writing code rocks"], ["writing code","code rocks"]],
    [["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"], ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]],
    [["a"], ["a","b","a"]]
]
solution = Solution()
for expected, phrases in test_cases:
    actual = solution.beforeAndAfterPuzzles(phrases)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: phrases: {phrases}")

print("Ran all tests")