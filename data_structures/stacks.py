'''
Stacks
    LIFO

Use Cases


Methods
    initialize the stack object Stack()
    push(val)
    pop()
    isEmpty()
    top()
    size()

'''


class Stack:
    def __init__(self) -> None:
        self.items = []
        self._size = 0

    def isEmpty(self) -> bool:
        return self._size == 0
    
    def push(self, val) -> None:
        self.items.append(val)
        self._size += 1
    
    def pop(self) -> int:
        if not self.isEmpty():
            rem = self.items.pop()
            self._size -= 1
            return rem
        raise IndexError

    def top(self) -> int:
        return self.items[-1]
    
    def size(self) -> int:
        return self._size
    

stack = Stack()

for i in range(5): # 0, 1, 2, 3, 4
    stack.push(str(i)+"A")

while not stack.isEmpty():
    print(stack.pop())
