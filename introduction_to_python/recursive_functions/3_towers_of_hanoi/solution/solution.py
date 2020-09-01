# Define a recursive Python function named `tower_of_hanoi`. The function consumes 4 arguments:
# * `n` - the number of disks
# * `from_rod` - the starting rod with all the disks (a list of integers representing the size of the disk)
# * `to_rod` - the desintation rod to end with all the disks
# * `aux_rod` - an auxiliary rod to assist with moving the disks

# The function returns the minimal number of moves required to get all the disks from `from_rod` to `to_rod`.

# Write your solution here
def tower_of_hanoi(n , from_rod, to_rod, aux_rod):
    if n <= 1:
        print(f"Move disk {n} from source ", from_rod, "to destination", to_rod)
        return n
    
    # Move n - 1 disks from source to auxiliary, so they are out of the way
    count = tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
            
    # Move the nth disk from source to target
    print(f"Move disk {n} from source {from_rod} to destination {to_rod}")
    to_rod.append(from_rod.pop())
    count += 1

    # Move the n - 1 disks that we left on auxiliary onto target
    count += tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)
    return count

# if n==1:
#     return 1
# else:
#     return (2**n)-1

# print(tower_of_hanoi(4, "A", "B", "C"))