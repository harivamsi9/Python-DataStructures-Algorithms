"""
POSSIBLE IMPROVEMENTS:
    1. NEED TO ADD COMMENTS FOR EACH METHOD IN THE CODE
    2. ADDING PROPER MULTIPLE RETURN TYPES FOR THE METHODS

"""

class Queue:
    '''
    Queue:
        FIFO

    Methods:
        initialize an object of class Queue()
        enque(item)
        deque()
        first()
        last()
        size()
        isEmpty()
    '''

    def __init__(self) -> None:
        self.items = []
        self._size = 0

    def _first(self) -> int:
        if not self.isEmpty():
            return self.items[0]
        raise IndexError
    
    def _last(self) -> int:
        if not self.isEmpty():
            return self.items[-1]
        raise IndexError
 
    def isEmpty(self) -> int:
        return self._size == 0
    
    def enque(self, item) -> None:
        self.items.append(item)
        self._size += 1
    
    def deque(self) -> int:
        if not self.isEmpty():
            out = self.items.pop(0)
            self._size -= 1
            return out
        raise IndexError("Index out of range")
    
    def size(self) -> int:
        return self._size
    
    def _print(self) -> list:
        return [i for i in self.items]
    

queue = Queue()
queue2 = Queue()


for i in range(5):
    print(i, end = ' ')
    queue.enque(i)
    queue2.enque(i)

print()
print()

for i in range(7):
    queue.deque()
    print(i, end = ' ')
    queue2.deque()
print()



# print(f"First: {queue._first()}")

# print(f"_print: {queue._print()}")
# print(queue2)

# print(queue == queue2)
# print(queue2)