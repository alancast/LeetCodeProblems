from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        self.preProcessWordList(wordList, len(beginWord))

        self.visitedStart = {beginWord: 1}
        self.visitedEnd = {endWord: 1}
        self.q_start = deque()
        self.q_end = deque()
        self.q_start.append(beginWord)
        self.q_end.append(endWord)
        answer = None

        while self.q_start and self.q_end:
            if len(self.q_start) <= len(self.q_end):
                answer = self.processNode(self.q_start, self.visitedEnd, self.visitedStart)
            else:
                answer = self.processNode(self.q_end, self.visitedStart, self.visitedEnd)

            if answer:
                return answer

        # We couldn't find the word        
        return 0

    def processNode(self, q: deque, other_visited: map, visited: map) -> int:
        q_size = len(q)
        for _ in range(q_size):
            word = q.popleft()
            if word in other_visited:
                return visited[word] + other_visited[word] - 1
            
            words = self.findWordsOffByOneBidrectional(word)
            for new_word in words:
                if new_word in visited:
                    continue
                visited[new_word] = visited[word] + 1
                q.append(new_word)

        return None

    def ladderLengthOneDirectional(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.preProcessWordList(wordList, len(beginWord))
        self.visited = set()
        q = deque()
        q.append([beginWord, 1])
        self.visited.add(beginWord)

        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            
            words = self.findWordsOffByOne(word)
            for new_word in words:
                q.append([new_word, count + 1])

        # We couldn't find the word        
        return 0
    
    def preProcessWordList(self, words: List[str], wordSize: int) -> None:
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)
        for word in words:
            for i in range(wordSize):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    def findWordsOffByOneBidrectional(self, start: str) -> List[str]:
        one_offs = []
        word_len = len(start)
        for i in range(word_len):
            next_words = self.all_combo_dict[start[:i] + "*" + start[i+1:]]
            for word in next_words:
                one_offs.append(word)

        return one_offs

    def findWordsOffByOne(self, start: str) -> List[str]:
        one_offs = []
        word_len = len(start)
        for i in range(word_len):
            next_words = self.all_combo_dict[start[:i] + "*" + start[i+1:]]
            for word in next_words:
                if word not in self.visited:
                    one_offs.append(word)
                    self.visited.add(word)

        return one_offs

testCases = [
    # ["hit", "cog", ["hot","dot","dog","lot","log","cog"], 5],
    ["hit", "cog", ["hot","dot","dog","lot","log"], 0],
    ["aaa", "bbb", ["abb","bbb"], 0],
    ["a", "b", ["b"], 2]
]
solution = Solution()
for beginWord, endWord, wordList, expected in testCases:
    answer = solution.ladderLength(beginWord, endWord, wordList)
    if answer != expected:
        print(f"FAILED TEST: Got {answer}, expected {expected}")
        print(f"INPUTS: begin: {beginWord}, end: {endWord}, list = {wordList}")