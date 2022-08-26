"""
362. Design Hit Counter
Medium

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds). Your system should accept a timestamp parameter (in seconds), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:
HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
"""


class HitCounter:

    def __init__(self):
        self.hits = collections.deque([])

    def hit(self, timestamp: int) -> None:
        """
        Records a hit that happened at timestamp (in seconds)
        """
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

    def getHits(self, timestamp: int, N=300) -> int:
        """
        Return the number of hits in the past 5 minutes.
        """
        while self.hits and self.hits[0][0] <= timestamp-N:
            self.hits.popleft()
        return sum([x[1] for x in self.hits])
