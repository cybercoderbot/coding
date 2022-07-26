"""
706. Design HashMap
Easy

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


class MyHashMap:
    def __init__(self):
        self.data = [None] * (10e6+1)

    def put(self, key: int, val: int) -> None:
        self.data[key] = val

    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val != None else -1

    def remove(self, key: int) -> None:
        self.data[key] = None


"""
705. Design HashSet
Easy

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.

"""


class MyHashSet:
    """
    Using List of Lists
    """

    def __init__(self):
        self.size = int(1e4)
        self.hashSet = [[] for i in range(self.size)]

    def getIndex(self, key) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.getIndex(key)
        if key not in self.hashSet[index]:
            self.hashSet[index].append(key)

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        if key in self.hashSet[index]:
            self.hashSet[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.getIndex(key)
        return key in self.hashSet[index]


class MyHashSet:
    """
    Using List of Sets
    """

    def __init__(self):
        self.size = int(1e4)
        self.hashSet = [set() for i in range(self.size)]

    def getIndex(self, key) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.getIndex(key)
        self.hashSet[index].add(key)

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        if key in self.hashSet[index]:
            self.hashSet[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.getIndex(key)
        return key in self.hashSet[index]


class MyHashSet:
    """
    Using List of deque
    """

    def getIndex(self, key) -> int:
        return key % self.size

    def __init__(self):
        self.size = int(1e4)
        self.hashSet = [collections.deque() for i in range(self.size)]

    def add(self, key: int) -> None:
        index = self.getIndex(key)
        if key not in self.hashSet[index]:
            self.hashSet[index].append(key)

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        if key in self.hashSet[index]:
            self.hashSet[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.getIndex(key)
        return key in self.hashSet[index]


class MyHashSet:
    def eval_hash(self, key):
        return ((key*1031237) & (1 << 20) - 1) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]
