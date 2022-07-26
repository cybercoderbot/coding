class MovingAverage(object):

    # 这道题定义了一个MovingAverage类，里面可以存固定个数字，然后我们每次读入一个数字，
    # 如果加上这个数字后总个数大于限制的个数，那么我们移除最早进入的数字，然后返回更新后的平均数，
    # 这种先进先出的特性最适合使用队列queue来做，而且我们还需要一个变量sum来记录当前所有
    # 数字之和，这样有新数字进入后，如果没有超出限制个数，则sum加上这个数字，如果超出了，那么sum先
    # 减去最早的数字，再加上这个数字，然后返回sum除以queue的个数即可

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """

        self.sum = 0
        self.size = size
        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)

        # self.queue.append(val)
        # if len(self.queue) <= self.size:
        #     self.sum += val
        # else:
        #     self.sum += val - self.queue.popleft()

        # return self.sum/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
