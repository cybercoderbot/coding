class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = self.helper(n, [])
        return [a for a in res if a[0] != '0'] if n != 1 else res

    def helper(self, n, res):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['00', '11', '69', '88', '96']
        res = []
        for ele in self.helper(2, res):
            cur = []
            for char in (self.helper(n-2, res)):
                cur.append(ele[0] + char + ele[1])
            res += cur
        return res

    #     if n==0: return ['']
    #     if n == 1: return ['0','1','8']
    #     if n==2: return ['00','11','69','88','96']

    #     return self.find(n, n)

    # def find(self, x, y):

    #     if x==0: return [""]
    #     if x==1: return ["0","1","8"]
    #     base = self.find(x-2, y)
    #     ans = []
    #     for s in base:
    #         if x!=y:
    #             ans.append("0"+ s +"0")
    #         ans.append(["1"+ s +"1", "6"+ s +"9", "8"+ s +"8", "9"+ s +"6"])
