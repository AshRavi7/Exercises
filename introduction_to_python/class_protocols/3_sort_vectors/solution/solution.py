from math import sqrt as sq
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"(x = {self.x}, y = {self.y}, z = {self.z})"

    def magnitude(self):
        return sq(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
    def __eq__(self, other):
        return self.magnitude() == other.magnitude()
    

def sort_vectors(vect_lst):
    n = len(vect_lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if vect_lst[j] > vect_lst[j+1] : 
                vect_lst[j], vect_lst[j+1] = vect_lst[j+1], vect_lst[j] 
    return vect_lst



# bubble sort
# def bubbleSort(arr): 
#     n = len(arr) 
#     # Traverse through all array elements 
#     for i in range(n-1): 
#     # range(n) also work but outer loop will repeat one time more than needed. 
#         # Last i elements are already in place 
#         for j in range(0, n-i-1): 
#             # traverse the array from 0 to n-i-1 
#             # Swap if the element found is greater 
#             # than the next element 
#             if arr[j] > arr[j+1] : 
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 