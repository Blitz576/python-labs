class Queue():
    def __init__(self):
        self._items = []
        self._front = -1
        self._rear = -1

    def enqueue(self, item):
        self._items.append(item)
        self._rear += 1
        if self._front == -1:
            self._front += 1

    def handleEmpty(self):
        if self.is_empty():
            self._front = -1
            self._rear = -1

    def dequeue(self):
        if self._front != self._rear:
            self._items.remove(self._items[self._front])
            self._rear = len(self._items) - 1
            self.handleEmpty()
        else:
            raise IndexError("Queue is empty")

    @property
    def front(self):
        return self._items[self._front]

    @property
    def rear(self):
        return self._items[self._rear]

    def is_empty(self):
        return len(self._items) == 0

# Test the Queue class
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.front)
print(queue.rear)
print(queue.is_empty())
queue.dequeue()
print(queue.front)
print(queue.rear)
