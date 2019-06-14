class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # The append method adds elements to the buffer
    def append(self, item):
        self.storage[self.current] = item

        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    # The get method returns all of the elements in the buffer in a list in their given order.
    # It should not return any None values in the list even if they are present in the ring buffer.
    def get(self):
        result = [i for i in self.storage if i is not None]
        return result
