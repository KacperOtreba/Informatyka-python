# def quicksortHoare(T, lewy, prawy):
#     i = lewy
#     j = prawy
#     pivot = T[(lewy+prawy)//2]

#     while i <= j:
#         while T[i] < pivot:
#             i = i + 1
#         while T[j] > pivot:
#             j = j - 1
#         if i <= j:
#             T[i], T[j] = T[j], T[i]
#             i = i + 1
#             j = j - 1
    
#     if lewy < j:
#         quicksortHoare(T, lewy, j)
#     if prawy > i:
#         quicksortHoare(T, i, prawy)


# from random import randint
# T = [randint(1, 100) for i in range(20)]
# print(T)
# quicksortHoare(T, 0, len(T)-1)
# print(T)