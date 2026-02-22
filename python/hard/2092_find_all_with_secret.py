from collections import defaultdict


class UnionFind:
    def __init__(self, n: int) -> None:
        # Zero indexed so add one
        self.parent = list(range(n+1))

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

    def does_person_know_secret(self, n: int) -> bool:
        return self.find(n) == 0

    def get_all_secret_knowers(self) -> list[int]:
        return [i for i in range(len(self.parent)) if self.does_person_know_secret(i)]

    def reset(self, x: int) -> None:
        # Reset the initial properties of node x
        self.parent[x] = x

    def union(self, n1: int, n2: int) -> None:
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return

        if p1 <= p2:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2

class Solution:
    # UnionFind, group all meetings in order of time, then join folks
    # Time O(nlogn)
    # Space O(n)
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # Sort meetings in increasing order of time
        meetings.sort(key=lambda x: x[2])

        # Group Meetings in increasing order of time
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        # Create union find and unite first person who knows secret
        uf = UnionFind(n)
        uf.union(firstPerson, 0)

        # Process meetings in increasing order of time
        for t in same_time_meetings:
            # Unite two persons taking part in a meeting
            for x, y in same_time_meetings[t]:
                uf.union(x, y)

            # If someone doesn't know secret reset them
            for x, y in same_time_meetings[t]:
                # No need to check for y since x and y were union-ed earlier
                if not uf.does_person_know_secret(x):
                    uf.reset(x)
                    uf.reset(y)

        return uf.get_all_secret_knowers()

test_cases = [
    [[0,1,2,3,5], 6, [[1,2,5],[2,3,8],[1,5,10]], 1],
    [[0,1,3], 4, [[3,1,3],[1,2,2],[0,3,3]], 3],
    [[0,1,2,3,4], 5, [[3,4,2],[1,2,1],[2,3,1]], 1]
]
solution = Solution()
for expected, n, meetings, first_person in test_cases:
    actual = solution.findAllPeople(n, meetings, first_person)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: n: {n}, meetings: {meetings}, first_person: {first_person}")

print("Ran all tests")
