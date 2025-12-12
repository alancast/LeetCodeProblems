from typing import List


class Solution:
    # Sort events by timestamp
    # Create an array for mentions
    # Process every message and increment array when mentioned
    # Create a count of here mentions
    # Create a set of offline users
    # Decrement mention increment when here is counted and offline
    # Time O(nlogn) for sorting events
    # Space O(num_users)
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Sort by timestamp, and for equal timestamps sort by message inverse (OFFLINE before MESSAGE)
        events.sort(key=lambda ev: (int(ev[1]), 0 if ev[0] == "OFFLINE" else 1))

        mention_count = [0] * numberOfUsers
        here_and_all_count = 0
        offline_map: dict[int, int] = {}

        # Process all messages
        for message, timestamp, mentions in events:
            # Update the offline map for the user going offline
            if message == "OFFLINE":
                offline_map[int(mentions)] = int(timestamp) + 60
                continue

            # It is a message, so process the 3 types
            if mentions == "ALL":
                here_and_all_count += 1
                continue
            # Decrement for all folks offline increment
            elif mentions == "HERE":
                here_and_all_count += 1
                time = int(timestamp)
                to_remove = set()

                # Decrement for all offline users
                for key, value in offline_map.items():
                    if value > time:
                        mention_count[key] -= 1
                    # This time has passed so user is back online
                    else:
                        to_remove.add(key)
                
                # Remove all back online users
                for id in to_remove:
                    offline_map.pop(id)

            # Parse out the ids mentioned
            else:
                id_strs = mentions.split(' ')
                for id_str in id_strs:
                    mention_count[int(id_str[2:])] += 1



        # Add here and all count to all mentions
        for i in range(numberOfUsers):
            mention_count[i] += here_and_all_count

        return mention_count

test_cases = [
    [[1,0,2], 3, [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]
],
    [[2,2], 2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]],
    [[2,2], 2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]],
    [[0,1], 2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]]
]
solution = Solution()
for expected, number_of_users, events in test_cases:
    actual = solution.countMentions(number_of_users, events)
    if expected != actual:
        print(f"FAILED TEST! Expected {expected} but got {actual}")
        print(f"\tINPUTS: number_of_users: {number_of_users}, events: {events}")

print("Ran all tests")