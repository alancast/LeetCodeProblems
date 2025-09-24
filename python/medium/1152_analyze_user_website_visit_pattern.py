from collections import defaultdict
from itertools import combinations
from typing import List


# Information about a site visit
class VisitNode:
    username: str
    timestamp: str
    website: str

    def __init__(self, username, timestamp, website):
        self.username = username
        self.timestamp = timestamp
        self.website = website


class Solution:
    # Just brute force
    # Sort on timestamp, then create lists for every user of websites they visit in order
    # Then create every possible pattern for every user and count them
    # Go over all pattern counts and return max
    # Time O(n^3)
    # Space O(n^3)
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        # Create visit nodes array purely to sort entries by timestamp
        visit_nodes = [
            VisitNode(name, ts, site)
            for name, ts, site in zip(username, timestamp, website)
        ]
        visit_nodes.sort(key=lambda x: x.timestamp)

        # Create a list of all websites visited by each user (in order)
        user_visits = defaultdict(list)
        for visit_node in visit_nodes:
            user_visits[visit_node.username].append(visit_node.website)

        # Count of times a visit pattern occurs
        # Key must be a tuple for it to work in dict
        visit_pattern_count = defaultdict(int)
        # For every user, create every possible pattern
        for website_visits in user_visits.values():
            # Create a set for all potential visit patterns for this user
            user_visit_patterns = set()
            for i, j, k in combinations(range(len(website_visits)), 3):
                pattern = (website_visits[i], website_visits[j], website_visits[k])
                user_visit_patterns.add(pattern)

            # Update pattern counts
            for pattern in user_visit_patterns:
                visit_pattern_count[pattern] += 1

        # Go over all patterns and find ones with the highest user count
        max_user_count = -1
        answer = ()
        for pattern, user_count in visit_pattern_count.items():
            # Have a new best pattern
            if user_count > max_user_count or (user_count == max_user_count and pattern < answer):
                max_user_count = user_count
                answer = pattern
        
        return list(answer)

test_cases = [
    [
        ["home","about","career"],
        ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
        [1,2,3,4,5,6,7,8,9,10],
        ["home","about","career","home","cart","maps","home","home","about","career"]
    ],
    [
        ["a","b","a"],
        ["ua","ua","ua","ub","ub","ub"],
        [1,2,3,4,5,6],
        ["a","b","a","a","b","c"]
    ]
]
solution = Solution()
for expected, usernames, timestamps, websites in test_cases:
    actual = solution.mostVisitedPattern(usernames, timestamps, websites)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: usernames: {usernames}, timestamps: {timestamps}, websites: {websites}")

print("Ran all tests")