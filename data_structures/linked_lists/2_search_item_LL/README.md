#  Search Item Exists

## Motivation
Since arrays require contiguous memory locations, it is very difficult to remove or insert an item in an array since the memory locations of a large number of items have to be updated. On the other hand, linked list items are not stored in a contiguous memory location, therefore you can easily update linked lists.

Owing to its flexibility, a linked list is more suitable for implementing data structures like stacks, queues, and lists.

## Problem Description
Write a program to create a linked list, push some items and check if the items exixts in the data structure. 

Build a Python class `Node` containing default instance `self.data`=None  and `self.next` to initialise the node object.Create another class `LinkedList` having 2 default instances `self.tail`=None, `self.head`=None and 1 instance variable `self.count`+=1.
Class `LinkedList` contains functions  `append` ,`iterate` and `search`.

Create LinkedList object `items` peforming some functions calls to `append` , iterate to check if a random data item exists and print `True` or `False`.


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
