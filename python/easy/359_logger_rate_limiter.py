class Logger:

    def __init__(self):
        # Key = message. Value = timestamp
        self.timeMap = {}

    # Time O(1) as constant lookup of hash map
    # Space O(n) as map will over time contain every message ever gotten
    # Would be good to purge every once in a while through various methods
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timeMap:
            self.timeMap[message] = timestamp
            return True
        
        # already printed message, check when
        if timestamp - self.timeMap[message] >= 10:
            self.timeMap[message] = timestamp
            return True
        
        return False
