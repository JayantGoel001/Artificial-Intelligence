class Stack:
    def __init__(self):
        self.topPosition = -1
        self.l = []

    def push(self, data):
        self.l.append(data)
        self.topPosition += 1

    def top(self):
        return self.l[self.topPosition]

    def pop(self):
        if self.topPosition != -1:
            self.l.pop()
            self.topPosition -= 1
        else:
            print("ERROR Empty Stack")

    def isEmpty(self):
        if self.topPosition == -1:
            return True
        else:
            return False


if __name__ == '__main__':
    n = int(input("Enter the number of items in stack:"))
    stack = Stack()
    for i in range(n):
        x = int(input())
        stack.push(x)

    print("Reversed Stack :\n")
    while not stack.isEmpty():
        print(stack.top(), end=" ")
        stack.pop()
