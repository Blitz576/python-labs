import queue
import outOfBoundryException as oo
class ExtendedQueue(queue.Queue):
    queue_counter = 0
    def __init__(self,size,name):
        super().__init__()
        print(self.__dict__)
        self.size = size
        self.name = name
        self.__class__.queue_counter += 1
    def number_of_objects(self):
        return self.__class__.queue_counter

    def enqueue(self, item):
        if len(self._items) < self.size:
            super().enqueue(item)
        else:
            raise oo.QueueOutOfRangeException("Queue size limit exceeded")

    def save(self, filename):
        with open(filename, 'w') as file:
         file.write(f"{self.name},{self.size}\n")

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, size = line.strip().split(',')
                cls(int(size), name)