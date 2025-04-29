from fprintx import printx





class Node:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    def __str__(self):
        return(f"Node({self.val}, next={self.next})")


class MyLinkedList:

    def __init__(self):
        # self.head = Node(30)
        self.head = None
        # self.display()

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1


    def addAtHead(self, val: int) -> None:
        if self.head:
            self.head = Node(val, _next=self.head)
        else:
            self.head = Node(val)
            

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            # self.display()
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        # self.display()
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: 
            self.addAtHead(val)
            return
        
        count = 0
        curr = self.head
        while curr:
            if count == index-1:
                curr.next = Node(val, _next=curr.next)
                return
            curr = curr.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        
        count = 0
        curr = self.head
        while curr.next and curr:
            if count == index-1:
                curr.next = curr.next.next
                return
            count += 1
            curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
# obj.addAtIndex(0,20)
# obj.addAtIndex(1,30)
obj.display()


param_1 = obj.get(1)
print(param_1)

obj.deleteAtIndex(1)
param_1 = obj.get(1)
print(param_1)