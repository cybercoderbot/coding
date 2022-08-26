class Solution:
    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
    	"""
    	528. Random Pick with Weight (weight based sampling)
    	"""
    	N = len(self.w)
        return random.choices(range(N), weights=self.w)[0]


class Solution:
    def __init__(self, weights: List[int]):
        self.N = len(weights)
        self.pdf = [w / sum(weights) for w in weights]
        self.cdf = self.pdf.copy()
        for i in range(1, self.N):
            self.cdf[i] += self.cdf[i-1]

    def pickIndex(self) -> int:
    	"""
    	528. Random Pick with Weight (weight based sampling)
    	"""
        target = random.random()
        for i, x in enumerate(self.cdf):
            if target < x:
                return i


class Solution:
    def __init__(self, cities: List[str], populations: List[int]):
        self.N = len(cities)
        self.cities = cities
        self.pdf = [p / sum(populations) for p in populations]
        self.cdf = self.pdf.copy()
        for i in range(1, self.N):
            self.cdf[i] += self.cdf[i-1]

    def pickIndex(self) -> int:
    	"""
    	Output city names based on population
    	"""
        rand = random.random()
        for i, x in enumerate(self.cdf):
            if rand < x:
                return self.cities[i]


"""
398. Random Pick Index

Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
"""


class Solution:
    def __init__(self, nums: List[int]):
	    self.seen = defaultdict(list)
	    for i, x in enumerate(nums):
	        self.seen[x].append(i)

	def pick(self, target: int) -> int:
	    return random.choice(self.seen[target])


class Solution:
    def __init__(self, nums: List[int]):
    	# seen: {value: all indexes}
        self.seen = defaultdict(list)
        for i, x in enumerate(nums):
            self.seen[x].append(i)

    def pick(self, target: int) -> int:
    	nsamples = len(self.seen[target])
    	idx = random.randint(0, nsamples-1)
        return self.seen[target][idx]


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        return random.choice([i for i, x in enumerate(self.nums) if x == target])


"""
Reservoir sampling is an online algorithm for uniformly choosing k random elements from a stream.
In our case, k=1 (we need to sample just one element). We create a reservoir and put there the first node. Then iterate over nodes and replace the node in the reservoir with the current one with probability 1/i, where i is the index of the current node. In the end, we end up with the reservoir containing a node chosen with the uniform probability 1/n, where n is the number of nodes.

Why does it work? Intuitively we can see that elements from the start of the list can get to the reservoir relatively easily since the probability is pretty high at the beginning. But to stay there they have to survive the whole list of elements in front of them. The actual math proof can be found in this article https://florian.github.io/reservoir-sampling/
"""

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
    	"""
    	382. Linked List Random Node
    	Return a random node's value from the linked list. 
    	Each node must have the same probability of being chosen.
    	1) If list length is unknown but static, you can simply precompute the length and 
    	generate random indices based on that. It is faster than the reservior sampling.
    	2) If the list length changes dynamically, reservior sampling is a good choice
    	"""
        i = 1
        head = self.head
        node = self.head
        while head.next:
            head = head.next
            i += 1
            if random.randint(1, i) == i:
                node = head
        return node.val


class Solution:
    def __init__(self, M: int, N: int):
        self.M = M
        self.N = N
        self.used = set()

    def flip(self) -> List[int]:
    	"""
    	519. Random Flip Matrix
    	Returns a random index [i,j] of the matrix where matrix[i][j] == 0 
    	and flips it to 1.
    	"""
        while True:
            r = random.randint(0, self.M-1)
            c = random.randint(0, self.N-1)
            if (r, c) not in self.used:
                self.used.add((r, c))
                return [r, c]

    def reset(self) -> None:
    	""" 
    	Resets all the values of the matrix to be 0.
    	"""
        self.used = set()
        

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        areas = [self.area(rect) for rect in self.rects]
        self.weights = [x / sum(areas) for x in areas]
            
    def area(self, rect):
    	x1, y1, x2, y2 = rect
    	return abs(x2-x1+1) * abs(y2-y1+1)

    def pick(self) -> List[int]:
    	"""
    	497. Random Point in Non-overlapping Rectangles
		Choose a rect based on area(weights), then choose a point inside it.
		The bigger the rectangle, the higher the probability of it getting chosen
		"""
		# random.choices returns a list, we extract the first (and only) element.
        rect = random.choices(population=self.rects, weights=self.weights, k=1)[0]

        x1, y1, x2, y2 = rect  
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
    

class Solution:
    def rand10(self) -> int:
    	"""
    	470. Implement Rand10() Using Rand7()
    	"""
        x = 0
        for i in range(10):
            x += rand7()
        return x % 10 + 1
        

class Solution(object):
    def rand10(self) -> int:
        """
        470. Implement Rand10() Using Rand7()
        """
        matrix = [[1, 2, 3, 4, 5, 6, 7],
                  [8, 9,10, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9,10, 1],
                  [2, 3, 4, 5, 6, 7, 8],
                  [9,10, 1, 2, 3, 4, 5],
                  [6, 7, 8, 9,10, 0, 0],  # Last 2 elements are invalid
                  [0, 0, 0, 0, 0, 0, 0]]  # Entire row is invalid
        while True:
            row = rand7() - 1
            col = rand7() - 1
            if (row == 5 and col >= 5) or row == 6:
                continue
            return matrix[row][col]    

class Solution:
    def rand10(self) -> int:
        """
        470. Implement Rand10() Using Rand7(). Rejection sampling
        When generating a number in the desired range, output it.
        Otherwise, reject it and resample again.
        rand7(): generates a uniform random integer within [1, 7].
        Write a rand10() that generates a uniform random integer within [1, 10]
        Solution: rand7() will get random 1 ~ 7
		(rand7() - 1) * 7 + rand7() - 1 will get random 0 ~ 48
		We discard 40 ~ 48, now we have rand40 equals to random 0 ~ 39.
		We just need to return rand40 % 10 + 1 and we get random 1 ~ 10.
        """
        x = 40
        while x >= 40:
            x = (rand7() - 1) * 7 + rand7() - 1
        return x % 10 + 1


class Solution:
    def randM(self, N, M)- > int:
        """
  		Generalized solution for creating randM() using randN()
		The randN() API is already defined for you.
		Return a random integer in the range 1 to M
        """
        # acceptable is the desired range which can generate required integer directly
        x = acceptable = N * N - (N * N) % M 
        # if x is not in the acceptable range, discard it and repeat the process again
        while x >= acceptable:
            x = (randN() - 1) * N + randN() - 1
        return x % M + 1
		

class Solution:
    def __init__(self, radius: float, x0: float, y0: float):
        self.radius = radius
        self.x0, self.y0 = x0, y0
        
    def randPoint(self) -> List[float]:
    	"""
    	478. Generate Random Point in a Circle
    	Polar coordinates
    	In polar coordinate system, f(r)~r and f(theta) = uniform[0, 2*pi). Leveraing on the fact that p(x)~uniform[0, 1) if x ~ p(x). We can sample r = R*sqrt(x) where x follows uniform distribution.
    	NO:  x = rand(R) * cos(rand(theta))
    	YES: x = sqrt(rand(R)) * cos(rand(theta))
    	"""
        theta = random.uniform(0, 2*pi)
        R = sqrt(random.uniform(0, self.radius ** 2))
        # R = self.radius * sqrt(random.uniform(0,1))
        return [self.x0 + R * cos(theta), self.y0 + R * sin(theta)]
   



