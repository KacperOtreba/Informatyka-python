# # 1 Funkcja ord() - zwraca kod ascii dla danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# # 2 funkcja chr() - zwraca znak dla danego kodu ascii
# print(chr(256))
# print(chr(75))
# print(chr(92))

# # można łączyć....
# print(chr(ord("H")))
# print(chr(ord("C")+5))

# napisz alfabet za pomocą petli for

# for i in range(65,89):
#   print(chr(i), end=" ")

# jak wydobyć literki z napisu
# napis = "POLSKA"
# print("Długość napisu: ", len(napis))
# print(napis[0])
# print(napis[1])

# napisz petle wyciagajaca z napisu literki

# napis = input("NO DAJ NAPIS: ")
# napis = napis.replace(" ", "")
# for i in range(len(napis)):
#   print(napis[i])

# napisz petle wyciągającą kody ascii z napisu
# napis = input()
# for i in range(len(napis)):
#   print(ord(napis[i]))

# zaszyfruj napis Cezarem dla kluczu = 3
napis = input("Podaj napis a ja go zaszyfruje: ")
szyfr = ""
for i in range(len(napis)):
  szyfr += chr((ord(napis[i]) - 65 + 3) % 26 + 65)
print(szyfr)














napis = input()
szyfr = ""
for i in range(len(napis)):
  szyfr += chr((ord(napis[i])-62)%26+65)
print(szyfr)