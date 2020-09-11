#  Delete Data End 

## Motivation
To delete an element from the end of the list, we simply have to iterate through the linked list till the second last element, and then we need to set the reference of the second last element to none, which will convert the second last element to last element.

## Problem Description
Write a program to delete data from the end of a user defined linked list structure.

Build a Python class `Node` containing default instance `self.data`=None  and `self.next` to initialise the node object.
Create another class `LinkedList` having instance `self.head`=None.

Build logic in class `LinkedList` having  functions  `traverse` to check if data exists and print data ,`insert_at_start` to insert data , `delete_at_end` to delete the data from the end of the data structure. 

Create LinkedList object `items` which performs functions calls to insert data items first , `delete_at_end` to delete the items and finally `traverse` to display the data.  

## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
