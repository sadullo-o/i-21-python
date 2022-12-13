# # 1. 
# davlatlar = ['Uzbekistan', 'Russian', 'USA', 'France', 'China', 'Brasil','Argentina']
# davlatlar.sort()
# # print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar1 = ['Uzbekistan', 'Russian', 'USA', 'France', 'China', 'Brasil','Argentina']
# print(sorted(davlatlar1))

# # 2. 
# sonlar = list(range(100,1001,2))
# print(f"Ro'yxatda {len(sonlar)} ta juft son bor, yigindisi {sum(sonlar)} ga teng")

# x = sonlar[0 : 21]
# z = (0 + len(sonlar))// 2  
# k = sonlar[z - 10 : z + 11]
# y = sonlar[len(sonlar)-20 : ]
# print(x + k + y)

# # 3. 
# taom = ['Osh', 'Manti',"Sho'rva", "Lag'mon", "Chuchvara", "Jarkob"]
# nonushta = taom[:]
# print(nonushta)

# for takrorlanuvchi operatori

# taom = ['Osh', 'Manti',"Sho'rva", "Lag'mon", "Chuchvara", "Jarkob"]

# print(taom[0])
# print(taom[1])
# print(taom[2])
# print(taom[3])
# print(taom[4])

# for a in taom: # taom ro'yxatida nechta element bo'lsa, tarkibdagi kod shuncha marta takrorlanadi
    # print('Taom: ')
    # print(a)


# for i in range(1, 11):
#     print(i)

# sonlar = list(range(1, 21))

# for x in sonlar:
#     print(x**2)


# kublar = []

# for x in sonlar:
#     kublar.append(x**3)

# print(kublar)


# ism = input('Ismingizni kiriting: ')

# print('Salom', ism)


# taom = input('Taomni kiriting: ')
# taom1 = input('Taomni kiriting: ')
# taom2 = input('Taomni kiriting: ')
# taom3 = input('Taomni kiriting: ')
# taom4 = input('Taomni kiriting: ')

# zakaz = []

# for i in range(1, 4):
#     taom = input(f'{i} - taomni kiriting')
#     zakaz.append(taom)

# print(zakaz)
# for i in range(1, 11):
#     print(i)



# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print('')

# son = int(input('Sonni kiriting: '))
# yigindi = 1

# for i in range(1, son+1):
#     yigindi *= i
# print(yigindi)


# n -->> 1 dan n gacha sonlar kopaytmasi


# numbers = [12, 75, 150, 180, 145, 525, 50]
# 5 ga qoldiqsiz bo'linadiganlari alohida print qilinsin

# numbers = [12,75,150,180,145,525,50]
# for i in numbers:
#     if not i%5:
#         print(i)

# for i in numbers:
#     if i%5 == 0:
#         print(i)



# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# m = 6
# for i in range(1, 6):
#     for j in range(m-i, 0, -1):
#         print(j, end=' ')
#     print('')

# list1 = [10, 20, 30, 40, 50]

# list1.reverse()

# for i in list1:
#     print(i)



# m = 6
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=' ') # 1 2 3 4 5

# asosiy for nechi kun mahsulot ishlab chiqarish
# ichidagi for nechtadan mahsulot ishlab chiqarish


# UYGA VAZIFA


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *



# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1




