class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 这道题给了我们一个数字，让我们对各个位数重新排序，求出刚好比给定数字大的一种排序，
        # 如果不存在就返回-1。这道题给的例子的数字都比较简单，我们来看一个复杂的，比如12443322，
        # 这个数字的重排序结果应该为13222344，如果我们仔细观察的话会发现数字变大的原因是左数第二位的2变成了3，
        # 后面的数字由降序变为了升序，这也不难理解，因为我们要求刚好比给定数字大的排序方式。
        # 我们再观察下原数字，看看2是怎么确定的，我们发现，如果从后往前看的话，2是第一个小于其右边位数的数字，
        # 因为如果是个纯降序排列的数字，做任何改变都不会使数字变大，直接返-1。知道了找出转折点的方法，再来看如何确定2和谁交换，
        # 这里2并没有跟4换位，而是跟3换了，那么如何确定的3？其实也是从后往前遍历，找到第一个大于2的数字交换，然后把转折点之后
        # 的数字按升序排列就是最终的结果了。最后记得为防止越界要转为长整数型，然后根据结果判断是否要返回-1即可
        
        
        if not n: return -1
        
        s = str(n)
        arr = [c for c in s]
        i = len(arr)-1
        
        while i > 0:
            if int(arr[i]) > int(arr[i-1]):
                j = i
                # looking for right position to swap
                while j < len(arr) and int(arr[j]) > int(arr[i-1]):
                    j += 1
                    
                arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
                j = len(arr)-1
                
                # reverse array from pivot point until end
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                    
                res = int(''.join(arr))
                
                # check 32 bit constraint
                return -1 if res > 2147483647 else res
            i -= 1
            
        return -1
        
        
        
