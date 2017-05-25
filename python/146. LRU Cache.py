class LRUCache(object):
    
    # OrderedDict有序字典法
    # https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
    
    # class collections.OrderedDict([items])
    # Return an instance of a dict subclass, supporting the usual dict methods. 
    # An OrderedDict is a dict that remembers the order that keys were first inserted. 
    # If a new entry overwrites an existing entry, the original insertion position is left unchanged. 
    # Deleting an entry and reinserting it will move it to the end.

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
        # The popitem() method for ordered dictionaries returns and removes a (key, value) pair. 
        # The pairs are returned in LIFO order if last is true or FIFO order if false.
            self.cache.popitem(False)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



