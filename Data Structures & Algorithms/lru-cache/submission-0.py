# Define a class Node with a key, value (passed in), previous, and next pointers (both None).
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # In the LRUCache init: 
        # 1. Initialize the capacity and cache.
        self.cap = capacity
        self.cache = {}

        # 2. Initialize left and right dummy nodes that point to each other.
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Define a remove function to remove a node.
    def remove(self, node):
        # The previous node is the passed in node's prev pointer.
        prev = node.prev
        # The next node is the passed in node's next pointer.
        nxt = node.next
        # The previous and next nodes we extracted should point to each other.
        prev.next = nxt
        nxt.prev = prev

    # Define an insert function to insert a node between the right dummy node and the node that it points back to.
    def insert(self, node):
        # The "previous" node is the right node's previous pointer.
        prev = self.right.prev
        # The "next" node is the right node itself.
        nxt = self.right
        # Make the previous and next nodes point to the new node.
        prev.next, nxt.prev = node, node
        # Make the new node point back to the previous and next nodes.
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        # In the get function:
        # If the key is in the cache, return the value of the key (which is a Node so get the value of the node).
        # Before returning, remove the node and re-insert it to make it the most recently used node.
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        # If the key doesn't exist, then return -1.
        return -1

    def put(self, key: int, value: int) -> None:
        # In the put function:
        # If the key exists in the cache, remove the existing node for that key,
        if key in self.cache:
            self.remove(self.cache[key])
        # In all cases, create a new node with the value,
        # assign it to the key in the cache,
        # insert it as the most recently used node.
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # If the length of the cache, exceeds the capacity,
        if len(self.cache) > self.cap:
            # get the LRU node (always the next pointer of the left node),
            lru = self.left.next
            # remove it,
            self.remove(lru)
            # and delete it from the cache (key = key of lru node)
            del self.cache[lru.key]

# Time: O(1) for get and put
# Space: O(n)

        
