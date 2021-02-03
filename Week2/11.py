class Queue:
    def __init__(self):
        self.l = []

    def enqueue(self, data):
        self.l.append(data)

    def dequeue(self):
        self.l = self.l[1:]

    def front(self):
        return self.l[0]

    def isEmpty(self):
        return len(self.l)==0


if __name__ == '__main__':
    n = int(input("Enter the number of items in queue:"))
    queue = Queue()
    for i in range(n):
        x = int(input())
        queue.enqueue(x)

    print("Queue :\n")
    while not queue.isEmpty():
        print(queue.front(), end=" ")
        queue.dequeue()
