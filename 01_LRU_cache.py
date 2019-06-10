class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

class LRU_Cache(object):
    def __init__(self, capacity):
        self.queue = Queue()
        self.cache = dict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            return self.cache[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if not (key in self.cache):
            if self.is_full():
                print("is full")
            else:
                self.cache[key] = value
    
    def is_full(self):
        return len(self.cache) == self.capacity

def test_expression(expression):
    print("pass" if expression else "fail")

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


# our_cache.get(1)       # returns 1
test_expression(our_cache.get(1) == 1)
# our_cache.get(2)       # returns 2
test_expression(our_cache.get(2) == 2)
# our_cache.get(9)      # returns -1 because 9 is not present in the cache
test_expression(our_cache.get(9) == -1)

our_cache.set(5, 5) 
our_cache.set(6, 6)

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3
test_expression(our_cache.get(3) == -1)


'''
references:
[1] key in dictonary complexity: https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
'''