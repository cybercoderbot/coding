"""
2073. Time Needed to Buy Tickets
Easy

There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

 
Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
"""

"""
Loop through all elements in list only once.

    (3) Any person nums[i] having tickets more than the k pos person, will buy tickets nums[i] times only.
    (2) Person nums[i] having tickets less than kth person ( nums[i] < least_tickets ), and standing before him(i<k), will be able to buy nums[i] amount.
    (1) Person nums[i] standing after kth person having more tickets than kth person, will be able to buy one less than the ticket kth person can buy(condition: least_tickets - 1).
"""


class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        res = 0
        for i, x in enumerate(nums):
            if i <= k:
                res += min(x, nums[k])
            else:
                res += min(x, nums[k]-1)
        return res


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k]-int(i > k), x) for i, x in enumerate(tickets))
