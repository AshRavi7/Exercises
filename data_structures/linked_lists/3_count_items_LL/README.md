#  Count Data Items

## Motivation
A linked list is a dynamic data structure which means that the memory reserved for the link list can be increased or reduced at runtime. No memory is allocated for a linked list data structure in advance. Whenever a new item is required to be added to the linked, the memory for the new node is created at run time. On the other hand, in case of the array, memory has to be allocated in advance for a specific number of items. In cases where sufficient items are not available to fill all array index, memory space is wasted.

## Problem Description
Write a program to create a linked list, push some items and display the count. 

Build a Python class `Node` containing default instance `self.data`=None  and `self.next` to initialise the node object.Create another class `LinkedList` having 2 default instances `self.tail`=None, `self.head`=None and 1 instance variable `self.count`+=1.
Class `LinkedList` contains 2 functions  `append` and `iterate`.

Create LinkedList object `items` peforming few calls to `append` ,finally iterate to print the items along with the total `count` value. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
