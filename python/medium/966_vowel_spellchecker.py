from typing import List


class Solution:
    # Keep dictionary of wordlist to answer
    # Search each word first by exact casing, then by all lowercase, then vowel replacing
    # Time O(n + q)
    # Space O(n)
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # For perfect mappings
        words_perfect = set()
        # Initialize word mapping
        word_mapping = dict()
        for word in wordlist:
            words_perfect.add(word)
            # Make sure there isn't already a lower case word this maps to
            word_lower = word.lower()
            if word_lower not in word_mapping:
                word_mapping[word_lower] = word
            # Make sure there isn't already a devowel this maps to
            word_lower_devowel = self._devowel(word_lower)
            if word_lower_devowel not in word_mapping:
                word_mapping[word_lower_devowel] = word

        # Go through each word in the queries to find mapping
        answer = []
        for query in queries:
            # Matches case exactly a word
            if query in words_perfect:
                answer.append(query)
                continue

            # Matches case independent
            lower_query = query.lower()
            if lower_query in word_mapping:
                answer.append(word_mapping[lower_query])            
                continue

            # Do vowel replacement
            devowel_lower = self._devowel(lower_query)
            if devowel_lower in word_mapping:
                answer.append(word_mapping[devowel_lower])            
                continue

            # No spellcheck replacement, just return empty string
            answer.append("")

        return answer
    
    # Replaces all instances of vowels with *
    def _devowel(self, word: str) -> str:
        return "".join('*' if c in 'aeiou' else c for c in word)

test_cases = [
    [
        ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
        ["KiTe", "kite", "hare", "Hare"],
        [
            "kite", "Kite", "KiTe", "Hare", "HARE",
            "Hear", "hear", "keti", "keet", "keto"
        ]
    ],
    [
        ["yellow"],
        ["yellow"],
        ["YellOw"]
    ],
    [
        ["ae"],
        ["ae","aa"],
        ["UU"]
    ]
]
solution = Solution()
for expected, word_list, queries in test_cases:
    actual = solution.spellchecker(word_list, queries)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: word_list: {word_list}, queries: {queries}")

print("Ran all tests")
