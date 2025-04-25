from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._count_of_substrings_fast_and_mem_efficient(word, k)
    
    # Time O(n) as we only call helper twice
    # Space O(1) as we only call helper twice
    def _count_of_substrings_fast_and_mem_efficient(self, word: str, k: int) -> int:
        return self._at_least_k(word, k) - self._at_least_k(word, k + 1)
    
    # Time O(n) as shrinking window goes over word twice
    # Space O(1) as we only keep vowel set
    def _at_least_k(self, word: str, k: int) -> int:
        n = len(word)
        num_substrings = consonant_count = start = end = 0
        vowel_count = defaultdict(int)

        # Compute substrings from sliding window
        while end < len(word):
            new_letter = word[end]
            if self._is_vowel(new_letter):
                vowel_count[new_letter] += 1
            else:
                consonant_count += 1

            # Add all the shrinking we can do for valid windows
            while (start < len(word) and len(vowel_count) == 5 and consonant_count >= k):
                # Add all substrings from here to end
                num_substrings += n - end

                # Remove letters til the substring breaks
                start_letter = word[start]
                if self._is_vowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_substrings
    
    # Time O(n) as shrinking window goes over word twice
    # Space O(n) as we keep next consonant array of size word
    def _count_of_substrings_fast_but_memory(self, word: str, k: int) -> int:
        num_substrings = consonant_count = start = end = 0
        vowel_count = defaultdict(int)
        # Array to compute index of next consonant for all indices
        next_consonant = [0] * len(word)
        next_consonant_index = len(word)

        # Create next_consonant array
        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._is_vowel(word[i]):
                next_consonant_index = i

        # Compute substrings from sliding window
        while end < len(word):
            new_letter = word[end]
            if self._is_vowel(new_letter):
                vowel_count[new_letter] += 1
            else:
                consonant_count += 1

            # Shrink window if too many consonants are present
            while consonant_count > k:
                start_letter = word[start]
                if self._is_vowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            # Add all the shrinking we can do for valid windows
            while (start < len(word) and len(vowel_count) == 5 and consonant_count == k):
                # Add all substrings that just append vowels (before next consonant)
                num_substrings += next_consonant[end] - end

                # Remove letters til the substring breaks
                start_letter = word[start]
                if self._is_vowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_substrings
    
    # Time O(n) as we just loop through the string once
    # Space O(k) as we keep a list of consonant indexes
    def _count_of_substrings_slow(self, word: str, k: int) -> int:
        n = len(word)
        left = num_substrings = 0
        # Map of vowel to when it most recently occured
        most_recent_vowel_occurrence = defaultdict(int)
        # List of consonant indexes
        consonant_indexes = []
        for i in range(n):
            char = word[i]
            # Process the char
            if self._is_vowel(char):
                most_recent_vowel_occurrence[char] = i
            else:
                consonant_indexes.append(i) 

            # Need more consonants
            if len(consonant_indexes) < k:
                continue

            # We have a substring, see how far forward left can go and still be valid
            if len(consonant_indexes) == k and len(most_recent_vowel_occurrence) == 5:
                # We can go as far forward as either losing a consonant or last occurrence of a vowel
                min_break = min(most_recent_vowel_occurrence['a'], most_recent_vowel_occurrence['e'], 
                                most_recent_vowel_occurrence['i'], most_recent_vowel_occurrence['o'], 
                                most_recent_vowel_occurrence['u'])
                if k > 0:
                    min_break = min(min_break, consonant_indexes[0])
                
                # Add num substrings count
                num_substrings += min_break - left + 1

            # Too many consonants, so move forward until we remove one
            if len(consonant_indexes) > k:
                left = consonant_indexes[0] + 1
                consonant_indexes.pop(0)

                # Either add new substrings or purge vowels that are gone
                min_break = min(most_recent_vowel_occurrence['a'], most_recent_vowel_occurrence['e'], 
                                most_recent_vowel_occurrence['i'], most_recent_vowel_occurrence['o'], 
                                most_recent_vowel_occurrence['u'])
                if k > 0:
                    min_break = min(min_break, consonant_indexes[0])
                if left <= min_break:
                    num_substrings += min_break - left + 1
                else:
                    # A vowel needs to be purged, not sure which one but one
                    if most_recent_vowel_occurrence['a'] < left:
                        del most_recent_vowel_occurrence['a']
                    if most_recent_vowel_occurrence['e'] < left:
                        del most_recent_vowel_occurrence['e']
                    if most_recent_vowel_occurrence['i'] < left:
                        del most_recent_vowel_occurrence['i']
                    if most_recent_vowel_occurrence['o'] < left:
                        del most_recent_vowel_occurrence['o']
                    if most_recent_vowel_occurrence['u'] < left:
                        del most_recent_vowel_occurrence['u']

        return num_substrings
    
    def _is_vowel(self, char: str) -> bool:
        return char in ["a", "e", "i", "o", "u"]
    
test_cases = [
    [2, "gqoajureim", 4],
    [0, "aeioqq", 1],
    [1, "aeiouh", 0],
    [1, "aeiou", 0],
    [1, "aeiouq", 1],
    [2, "aaeiouq", 1],
    [2, "qaeiouq", 1],
    [3, "ieaouqqieaouqq", 1]
]
solution = Solution()
for expected, word, k in test_cases:
    actual = solution.countOfSubstrings(word, k)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: word: {word}, k: {k}")

print("Ran all tests")