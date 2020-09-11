# def tower_of_hanoi(n , from_rod, to_rod, aux_rod):
#     if n <= 1:
#         return n
#     else:
#         count = tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
#         to_rod.append(from_rod.pop())
#         count += 1
#         count += tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)
#         return count

    
