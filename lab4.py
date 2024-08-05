#QUESTION 01 STACK IMPLEMENTATION
class Stack:
    """Implementation of a Stack"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def length(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.length() == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)
    

myStack = Stack()
myStack.push(5)
myStack.push(6)
print(myStack.peek())
print(myStack)

print("-----------------------------------------------------------")
#QUESTION 2 IMPLEMENTATION OF QUEUE
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
print("Is queue empty?", q.is_empty()) 

q.enqueue(4)
q.enqueue(9)
q.enqueue(2)
q.enqueue(10)

print("Is queue empty?", q.is_empty()) 
print("Size of queue is:", q.size())
print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("Dequeued : ",q.dequeue())
print("Dequeued : ",q.dequeue())

print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("---------------------------------------------------------------------------------------------")
#QUESTION 3 BINARY SEARCH
#ITERATIVE METHOD
def find(start, end, val, list):
    while start <= end:
        mid = (start + end) // 2
        if val == list[mid]:
            return mid
        elif val > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.")

#RECURSIVE METHOD
""" def find(start, end, val, list):
    if start > end:
        return -1
    mid = (start + end) // 2
    if val == list[mid]:
        return mid
    elif val > list[mid]:
        return find(mid + 1, end, val, list)
    else:
        return find(start, mid - 1, val, list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.") """
