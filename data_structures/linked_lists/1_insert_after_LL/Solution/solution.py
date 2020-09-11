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
    
    def insert_after_item(self, x, data):

        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


if __name__=='__main__':
    items =LinkedList()
   
    items.insert_at_start('40')
    items.insert_at_start('50')

    items.insert_after_item('50','0')

    items.traverse()