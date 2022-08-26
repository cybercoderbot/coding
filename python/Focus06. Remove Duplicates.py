class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        """
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        True if nums[i] == nums[j]
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        219. Contains Duplicate II
        True if nums[i] == nums[j] and abs(i - j) <= k
        """
        seen = defaultdict(int)
        for i, x in enumerate(nums):
            if x in seen and i - seen[x] <= k:
                return True
            seen[x] = i
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        220. Contains Duplicate at distance k within delta t
        True if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k
        Put numbers in a given range into bucket (k). Bucketing numbers properly, this 
        becomes similar to 219, except that numbers in adjacent buckets need to be checked 
        as well.
        """
        if t < 0:
            return False
        seen = {}
        for i, x in enumerate(nums):
            b = x // (t+1)
            if b in seen and i-seen[b][0] <= k:
                return True
            for y in b-1, b+1:
                if y in seen and i-seen[y][0] <= k and abs(x-seen[y][1]) <= t:
                    return True
            seen[b] = (i, x)
        return False


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        287. Find the Duplicate Number
        O(N) time, O(1) space
        """
        for x in nums:
            if nums[abs(x)] < 0:
                return abs(x)
            nums[abs(x)] *= -1


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        442. Find All Duplicates in an Array
        [1,1,2] -> [1], [4,3,2,7,8,2,3,1] -> [2,3]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] > 0:
                nums[abs(x)-1] *= -1
            else:
                res.append(abs(x))
        return res


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        26. Remove Duplicates from Sorted Array
        nums = [0,0,1,1,1,2,2,3,3,4] -> nums = [0,1,2,3,4,_,_,_,_,_], k=5
        """
        k, N = 1, len(nums)
        for i in range(N-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
        return k


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        80. Remove Duplicates from Sorted Array II (at most twice)
        """
        for x in nums:
            count = nums.count(x)
            if count > 2:
                for j in range(count-2):
                    nums.remove(x)
        return len(nums)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
        """
        19. Remove Nth Node From End of List
        """
        first = head
        for i in range(N):
            first = first.next
        if not first:
            return head.next

        second = head
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        83. Remove Duplicates from Sorted Linked List
        head =[1,1,2] -> [1,2], head = [1,1,2,3,3] -> [1,2,3]
        """
        node = head
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        82. Remove Duplicates from Sorted List II (delete all duplicates)
        head =[1,1,2] -> [2], head = [1,1,2,3,3] -> [2]
        """
        if not head or not head.next:
            return head

        freq = defaultdict(int)
        node = head
        while node:
            freq[node.val] += 1
            node = node.next
        nums = [k for k, v in freq.items() if v == 1]
        node = dummy = ListNode(None)
        for x in nums:
            node.next = ListNode(x)
            node = node.next
        return dummy.next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """
        1836. Remove Duplicates From an Unsorted Linked List
        head = [1,2,3,2] -> [1,3], head = [2,1,1,2] -> []
        """
        freq = defaultdict(int)
        node = head
        while node:
            freq[node.val] += 1
            node = node.next

        dummy = node = ListNode(next=head)
        while node.next:
            if freq[node.next.val] > 1:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        316. Remove Duplicate Letters
        'bcabc' -> 'abc', 'cbacdcbc' ->'acdb'
        """
        index = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c < stack[-1] and i < index[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(str(x) for x in stack)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        1047. Remove All Adjacent Duplicates In String
        s = "abbaca" -> "ca", s = "azxxzy" -> "ay"
        """
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        1209. Remove All Adjacent Duplicates in String II (at most k)
        """
        stack = []  # stack: (c, freq)
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return ''.join(c * x for c, x in stack)


class Solution:
    def minRemoveToMakeValid(self, s):
        """
        1249. Minimum Remove to Make Valid Parentheses
        'a)b(c)d' -> 'ab(c)d'
        """
        stack = []
        res = list(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    res[i] = ""

        for i in stack:
            res[i] = ""
        return '' .join(res)


class Solution:
    def trimMean(self, nums: List[int]) -> float:
        """
        1619. Mean of Array After Removing Some Elements
        Sort nums and compute the mean of middle 90%.
        """
        N = len(nums) // 20
        timmed = sorted(nums)[N:-N]

        return sum(timmed)/(len(timmed))
