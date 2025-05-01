

class Node:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    def __str__(self):
        return(f"Node({self.val}, next={self.next})")


class Stack:

    def __init__(self):
        # self.head = Node(30)
        self.head = None
        # self.display()
    
    def push(self, node):
        node = Node(node)
        node.next = self.head
        self.head = node

    def pop(self):
        self.head = self.head.next

    def peek(self):
        if self.head: return self.head.val
        return -1
    

    def display(self, node):
        curr = self.head
        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next

    def is_empty(self):
        return not bool(self.head)
        

obj = Stack()
obj.push(1)
obj.push(3)
obj.push(4)
obj.display()
obj.pop()
obj.pop()
obj.pop()
obj.display()
print(obj.peek())
print(obj.is_empty())


