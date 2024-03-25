# x = float(input("Wprowadź nominał: "))
# T = [500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
# print("Aby wydać poprawnie ten nominał musisz wziąść:")
# for item in T:
#     if x >= item:
#         ile = x//item
#         x -= ile * item
#         print(f"{item}zł {ile} razy")


############### KASA FISKALNA #####################

# zaplata = int(input("Ile kosztuje: "))
# dal = int(input("Ile klient dał kasy: "))
# x = dal - zaplata
# T = [50,20,10,5,2,1]
# print("Aby wydać poprawnie reszte musisz wziąść:")
# for item in T:
#     if x > item:
#         ile = x//item
#         x -= ile * item
#         print(f"{item}zł {ile} razy")

#####################################################


# x = int(input("Wprowadź nominał: "))
# W = []
# T = [500,200,100,50,20,10,5,2,1]
# print("Aby wydać poprawnie ten nominał musisz wziąść:")
# for item in T:
#     if x > item:
#         ile = x//item
#         x -= ile * item
#         for i in range(ile):
#             W.append(item)
# print(W)    