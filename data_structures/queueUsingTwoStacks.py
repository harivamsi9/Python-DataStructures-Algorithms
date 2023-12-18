'''
Queues Using Two Stacks
    FIFO
        Using 2 LIFO's
    q.enqueue(1)
    s1 = [1]
    s2 = []
    q.enqueue(2)
    s1 = [1,2]
    s2 = []
    q.enqueue(3)
    s1 = [1,2,3]
    s2 = []
    q.enqueue(4)
    s1 = [1,2,3,4]
    s2 = []

    q.dequeue()
    s1 = [1,2,3,4]
    pop each from s1, and push to s2
    s2 = [4,3,2,1]
    s2.pop()
    s2 = [4,3,2]
    push s2 back to s1
    q.dequeue()
    q.dequeue()
'''


class Queue2Stacks:
    def __init__(self) -> None:
        ## Pretend that the below lists only act like stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item) -> None:  # TC - O(1)
        self.stack1.append(item)
        return

    def dequeue(self) -> int:  # TC - O(n)
        for i in range(len(self.stack1)):
            item = self.stack1.pop()
            self.stack2.append(item)
        pop_item = self.stack2.pop()

        for i in range(len(self.stack2)):
            p = self.stack2.pop()
            self.stack1.append(p)
        return pop_item



# Testing
q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

'''
Expected Output:
0
1
2
3
4
'''