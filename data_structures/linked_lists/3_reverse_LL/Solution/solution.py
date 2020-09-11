class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data," ")
                n=n.next
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head= new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

    def reverse(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev
    
if __name__=='__main__':
    items =LinkedList()
   
    items.insert_at_start('100')
    items.insert_at_start('200')
    items.insert_at_end('300')
    items.insert_at_end('400')

    items.reverse()

    items.traverse()



