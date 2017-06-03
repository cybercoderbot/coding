class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, res):
            if pos == len(word):
                # Once we reach the end, append current to the result
                res.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, res)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, res)

        res = []
        helper(word, 0, '', 0, res)
        return res
        
        
        
