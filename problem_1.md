## LRU CACHE ##

### Adding key and value ###
This problem was solved using a combination with a hashmap and a Queue. Each value is added with the respective key to the cache, adding the value to a node object and put it in the queue and hash map (referenced by the key), so this operation has a time complexity of O(1), and space is proportional to the space, in conclution, the result is O(n).

### Asking value ###
The Queue use double linked nodes to store the values. When a value is asked to the cache using the key, in that node we removed from the linked list used in the Queue, and add it again using the enqueue method. This operation also has a time complexity of O(1).