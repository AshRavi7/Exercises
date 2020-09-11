class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def iterate(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def search(self, val):
         # Search the list
         for node in self.iterate():
             if val == node:
                 return True
         return False

if __name__=='__main__':
    items =LinkedList()
    items.append('50')
    items.append('60')
    items.append('70')
    items.append('80')
    if items.search('60'):
        print("True")
    else:
        print("False")