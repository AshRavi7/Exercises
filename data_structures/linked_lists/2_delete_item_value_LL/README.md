#  Delete Item Value

## Motivation
Deletion by Item Value

To delete the element by value, we first have to find the node that contains the item with the specified value and then delete the node. Finding the item with the specified value is pretty similar to searching the item. Once the item to be deleted is found, the reference of the node before the item is set to the node that exists after the item being deleted.

## Problem Description
Write a program to delete a data value from a linked list structure.

Build a Python class `Node` containing default instance `self.data`=None  and `self.next` to initialise the node object.
Create another class `LinkedList` having instance `self.head`=None.

Build logic in class `LinkedList` having  functions  `traverse` to print data ,`insert_at_start` to insert data , `delete_item_by_value` to delete the data from the end of the data structure. 

Create LinkedList object `items` which performs functions calls to insert data items , `delete_item_by_value` to delete the item value and finally  `traverse` to display the data.  

## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
