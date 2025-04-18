from collections import Counter
from math import factorial


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.validate_input(tiles)
        return self.num_tile_possibilities_gen_perms(tiles)
    
    # Time O(n * 2^n) each letter could or could not be in and factorial takes O(n) time
    # Space O(n * 2^n) call stack size n and seen set worst case could be all unique strings
    def num_tile_possibilities_gen_perms(self, tiles: str) -> int:
        seen = set()

        # Sort characters to handle duplicates efficiently
        sorted_tiles = "".join(sorted(tiles))

        # Find all unique sequences and their permutations
        return self._generate_sequences(sorted_tiles, "", 0, seen) - 1

    def _count_permutations(self, seq: str) -> int:
        # Math of this function follows the formula:
        # if we have 3 characters with frequencies n1, n2, and n3, 
        # the number of 3 length sequences are: (n1 + n2 + n3)!/(n1!*n2!*n3!))

        # Calculate permutations using factorial formula
        total = factorial(len(seq))

        # Divide by factorial of each character's frequency
        for count in Counter(seq).values():
            total //= factorial(count)

        return total

    def _generate_sequences(self, tiles: str, current_str: str, pos: int, seen: set) -> int:
        if pos >= len(tiles):
            # If new sequence found, count its unique permutations
            if current_str not in seen:
                seen.add(current_str)
                return self._count_permutations(current_str)
            return 0

        # Try including and excluding current character
        return self._generate_sequences(tiles, current_str, pos + 1, seen) + self._generate_sequences(tiles, current_str + tiles[pos], pos + 1, seen)
    
    # Time O(n!) as we get all combinations of tiles length n
    # Space O(n) as we only keep char count array which is O(1) and call stack can be n deep
    def num_tile_possibilities_better_recursion(self, tiles: str) -> int:
        # Track frequency of each uppercase letter (A-Z)
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord("A")] += 1

        # Find all possible sequences using character frequencies
        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: list) -> int:
        total = 0

        # Try using each available character
        for pos in range(26):
            if char_count[pos] == 0:
                continue

            # Add current character and recurse
            total += 1
            char_count[pos] -= 1
            total += self._find_sequences(char_count)
            char_count[pos] += 1

        return total

    # Time O(n!)
    # Space O(n!) as sequences set could be big
    def num_tile_possibilities_recursion(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)

        # Generate all possible sequences including empty string
        self._generate_sequences_recursion(tiles, "", used, sequences)

        # Subtract 1 to exclude empty string from count
        return len(sequences) - 1

    def _generate_sequences_recursion(self, tiles: str, current: str, used: list, sequences: set) -> None:
        sequences.add(current)

        # Try adding each unused character to current sequence
        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self._generate_sequences_recursion(tiles, current + char, used, sequences)
                used[pos] = False

    def validate_input(self, tiles: str) -> None:
        if len(tiles) < 1 or len(tiles) > 7:
            raise ValueError("tiles must be between length 1 and 7")
    
test_cases = [
    [8, "aab"],
    [1, "a"],
    [188, "aaabbc"]
]
solution = Solution()
for expected, tiles in test_cases:
    actual = solution.numTilePossibilities(tiles)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}. INPUTS: tiles: {tiles}")

print("Ran all tests")