class Node:
    # Function to initialise the node object 
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null 

# Linked List class contains a Node object 
class LinkedList:

    # Function to initialize head 
    def __init__(self):
        self.head = None
    
    # def __str__(self):
    #     n=self.head
    #     while n is not None:
    #         return f'{n.data}'
    #         n=n.next
    
    def traverse(self):
        if self.head is None:
            return
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.next
    
    def insert_at_start(self, data):
        new_node = Node(data) # data=50; self.data=50,self.next=None-> self.data=40,self.next=None
        new_node.next = self.head # self.next=None
        self.head= new_node # self.head=50 

   
    def delete_at_end(self):
        if self.head is None:
            return

        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

if __name__=='__main__':
    items =LinkedList()
   
    items.insert_at_start(50)
    items.insert_at_start(40)
    items.insert_at_start(30)
    items.insert_at_start(20)
    items.delete_at_end()

    items.traverse()