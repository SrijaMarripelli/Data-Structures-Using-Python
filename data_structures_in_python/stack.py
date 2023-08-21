class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        for item in self.stack:
            print(item)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
