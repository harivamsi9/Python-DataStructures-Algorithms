'''
Deque
    linear data structure, no ordering.
    you can add the items from the front and from the back
    you can remove the items from the front and the back

Methods
    initialize an empty Deque()
    /push_front(item)
    /push_back(item)
    /pop_front()
    /pop_back()
    /size()
    /front()
    /back()
    /isEmpty()    
'''


class Deque:
    def __init__(self) -> None:
        """Creates the empty Deque object"""
        self.items = []
        self._size = 0
    
    def _front(self) -> int:
        """Returns the front value of the Deque object"""
        if not self.isEmpty():
            return self.items[0]
        raise IndexError("Deque should have atleast 1 element to show the front")

    def _back(self) -> int:
        """Returns the back value of the Deque object"""
        if not self.isEmpty():
            return self.items[-1]
        raise IndexError("Deque should have atleast 1 element to show the back")

    def size(self) -> int:
        """Returns the size of the Deque object"""
        return self._size
    
    def isEmpty(self) -> bool:
        """Returns True is deque object is empty, else returns False"""
        return self._size == 0
    
    def push_front(self, item) -> None:
        """Pushes the item to the front of the deque object"""
        self.items.insert(0, item)
        self._size += 1
        return
    
    def push_back(self, item) -> None:
        """Pushes the item to the back of the deque object"""
        self.items.append(item)
        self._size += 1
        return
    
    def pop_front(self) -> int:
        """Returns the popped element from the front of the deque"""
        if not self.isEmpty():
            out= self.items.pop(0)
            self._size -= 1
            return out
        raise IndexError("Deque should contain atleast 1 element in it to pop")
    
    def pop_back(self) -> int:
        """Returns the popped element from the back of the deque"""
        if not self.isEmpty():
            out= self.items.pop()
            self._size -= 1
            return out
        raise IndexError("Deque should contain atleast 1 element in it to pop")
    
    def _print(self):
        print([i for i in self.items])
        return
    



### Testing
dq = Deque()
# print(dq)

# add to front; print sizes after you add; print Front and Back.
for i in range(5):  # [0,1,2,3,4]
    dq.push_front(i)
    print(f"i:{i}, size: { dq.size() }, front: {dq._front()}, back: {dq._back()}")
# dq = [4,3,2,1,0]
print('*'*10)
# add to back; print sizes after you add; print Front and Back.
for i in range(5): # [0,1,2,3,4]
    dq.push_back(i)
    print(f"i:{i}, size: { dq.size() }, front: {dq._front()}, back: {dq._back()}")
# dq = [4,3,2,1,0,0,1,2,3,4]
print('*'*10)
# add alternatively to front and back; print sizes after you add; print front and Back.
for i in range(10): # [0,1,2,3,4,5,6,7,8,9]
    dq.push_front(i)
    dq.push_back(i)
    print(f"i:{i}, size: { dq.size() }, front: {dq._front()}, back: {dq._back()}")
print('*'*10)
# dq = [9,8,7,6,5,4,3,2,1,0,4,3,2,1,0,0,1,2,3,4,0,1,2,3,4,5,6,7,8,9]

# remove alternatively to front and back; print sizes after you remove; print front and Back.
for i in range(10):
    dq.pop_front()
    dq.pop_back()
    print(f"i:{i}, size: { dq.size() }, front: {dq._front()}, back: {dq._back()}")

print('*'*10)
# dq = [4,3,2,1,0,0,1,2,3,4]
dq._print()

