class ValidWordAbbr(object):

    # 这道题让我们求独特的单词缩写，但是题目中给的例子不是很清晰，我们来看下面三种情况：
    # 1. dictionary = {"dear"},         isUnique("door") -> false
    # 2. dictionary = {"door", "door"}, isUnique("door") -> true
    # 3. dictionary = {"dear", "door"}, isUnique("door") -> false

    # 从上面三个例子我们可以看出，当缩写一致的时候，字典中的单词均和给定单词相同时，那么返回true。
    # 我们需要用哈希表来建立缩写形式和其对应的单词的映射，把所有缩写形式的相同单词放到一个dict中，
    # 然后我们在判断是否unique的时候只需要看给定单词的缩写形式的是否和dict中的缩写相同，相同的话
    # 就是上面的第二种情况，返回true。需要注意的是由于set中不能有重复值，
    # 所有上面第二种情况只会有一个door存在set里，但是并不影响判断结果

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = {}
        for w in dictionary:
            if len(w) <= 2:
                self.d[w] = [w]
            else:
                s = w[0] + str(len(w)-2) + w[-1]
                if s not in self.d:
                    self.d[s] = [w]
                else:
                    self.d[s].append(w)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) <= 2:
            val = word
        else:
            val = word[0] + str(len(word)-2) + word[-1]

        return val not in self.d or (len(self.d[val]) == 1 and self.d[val][0] == word)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
