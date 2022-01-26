class Queue():
    def __init__(self):
        self.data = list()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)



queue = Queue()
queue.enqueue(2)
queue.enqueue(0)
queue.enqueue(8)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
