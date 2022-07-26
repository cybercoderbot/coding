class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # 这道题让简化给定的路径，光根据题目中给的那一个例子还真不太好总结出规律，
        # 应该再加上两个例子 path = "/a/./b/../c/", => "/a/c"和path = "/a/./b/c/", => "/a/b/c"，
        # 这样我们就可以知道中间是"."的情况直接去掉，是".."时删掉它上面挨着的一个路径，
        # 而下面的边界条件给的一些情况中可以得知，如果是空的话返回"/"，如果有多个"/"只保留一个。
        # 那么我们可以把路径看做是由一个或多个"/"分割开的众多子字符串，把它们分别提取出来一一处理即可

        stack = []
        split_path = path.split('/')

        for e in split_path:
            if e in ('', '.'):
                pass
            elif e == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(e)

        return '/' + '/'.join(stack)
