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


if __name__=='__main__':
    items =LinkedList()
   
    items.insert_at_start('40')
    items.insert_at_start('50')
    items.insert_at_end('30')
    items.insert_at_end('20')


    items.traverse()