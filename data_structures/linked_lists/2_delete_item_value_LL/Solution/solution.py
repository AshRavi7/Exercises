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

   
    def delete_item_by_value(self, x):
        if self.head is None:
            return

    # Deleting first node 
        if self.head.data == x:
            self.head= self.head.next
            return

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

        if n.next is None:
            print("item not found in the list")
        else:
            n.next = n.next.next

if __name__=='__main__':
    items =LinkedList()
   
    items.insert_at_start('50')
    items.insert_at_start('40')
    items.insert_at_start('30')
    items.insert_at_start('20')
    items.delete_item_by_value('40')

    items.traverse()