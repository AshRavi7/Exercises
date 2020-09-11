#  Index Insertion 

## Motivation
However, there are some downsides to the linked list as well.

Since each linked list item has to store the reference to the next item, some extra memory is required.
    
Unlike Arrays, where you can directly access an item, you cannot access a linked list item directly since the only information you have is the reference to the first item. In Big O terms, worst-case access time is O(n).

## Problem Description
Write a program to insert data into the linked list structure at a random indexing position. 

Build a Python class `Node` containing default instance `self.data`=None  and `self.next` to initialise the node object.
Create another class `LinkedList` having instance `self.head`=None.

Build logic in class `LinkedList` having  functions  `traverse` ,`insert_at_start` , `insert_at-end`  and `insert_at_index`.

Create LinkedList object `items` peforming functions calls to insert data items at random and also append data at a certain index value , finally call function `traverse` to display the items. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
