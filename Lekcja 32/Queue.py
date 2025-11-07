class Queue:
    def __init__(self):
        self.queue = []
        pass

    def enqueue(self, item):
        self.queue.append(item)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    
    def size(self):
        return len(self.queue)


queue = Queue()

queue.enqueue("Klient 1")
queue.enqueue("Klient 2")
queue.enqueue("Klient 3")
queue.enqueue("Klient 4")


print(queue.queue)

while not queue.is_empty():
    print(queue.dequeue())
    print(queue.queue)