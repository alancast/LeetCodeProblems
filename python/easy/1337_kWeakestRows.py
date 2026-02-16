import heapq


class Solution:
    # Binary Search
    # O(m*log(nk)) time and O(k) space
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Calculate the strength of each row using binary search.
        # Put the strength/index pairs into a priority queue.
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)

        # Pull out and return the indexes of the smallest k entries.
        # Don't forget to convert them back to positive numbers!
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)
            indexes.append(-i)

        # Reverse, as the indexes are around the wrong way.
        return indexes[::-1]

    # Vertical indexing
    # O(mn) time and O(k) space
    # could be O(1) space if we just check if entry to left was also 0 instead of keeping set
    def kWeakestRowsVertical(self, mat: list[list[int]], k: int) -> list[int]:
        if not mat or not mat[0]:
            return []

        answer = []
        weakest = set()
        rows = len(mat)
        cols = len(mat[0])
        for i in range(cols):
            for j in range(rows):
                if j in weakest:
                    continue

                if mat[j][i] == 0:
                    answer.append(j)
                    weakest.add(j)
                    if len(answer) == k:
                        return answer

        # If remaining rows have all 1's add them to k weakest
        for i in range(rows):
            if i in weakest:
                continue

            answer.append(i)
            if len(answer) == k:
                return answer

        raise Exception("K not met despite done processing")

testCases = [
    [[
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]],
        3,
        [2,0,3]],
    [[
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]],
        2,
        [0,2]],
    [[
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,1,1,1]],
        3,
        [0,2,1]],
    [[
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,1,1,1]],
        4,
        [0,2,1,3]]
]
implementation = Solution()
for mat, k, expected in testCases:
    answer = implementation.kWeakestRows(mat, k)
    if answer != expected:
        print(f"FAILED TEST: Expected {expected} but got {answer}. INPUTS: mat: {mat} k: {k}")

print("Ran all tests")
