# UYGA VAZIFA KODI

# viloyat = input("Viloyatingizni kiriting  ")
# tuman = input("Tumaningizni kiriting  ")
# mahalla =  input("Mahallangizni kiriting  ")
# uy = input("Uyingiz raqamini kiriting  ")
# print(f'Manzil: {viloyat.capitalize()} viloyati, {tuman.capitalize()}  tumani, {mahalla.capitalize()} mahallasi, {uy}-uy')


# a = 15
# b = 28
# print(a**2,b**2,a**3,b**3)


#Lesson 2 Ro'yxatlar bilan ishlash

# a = 'olma'
# b = 15
# c = 14.6

# ruyxat turi - list
# sonlar = [45, 12, 532, 54,123, 34, 12, 45,5]
# sozlar = ['olma', 'kitob', 'shahar', 'havo', 'suv']
# aralash = ['kitob', 34, 10.5, -12, 0, 'havo', 'Toshkent chiroyli shahar']

# print(sonlar)
# print(sozlar[3])

# print(sonlar[6])

# print(aralash[4])
# print(sonlar[2] + sonlar[5])

# print(sozlar[3]+' juda sovuq')


# aralash = ['kitob', 34, 20, 'alifbo', 0, 'havo']

# aralash[2] = 25

# print(aralash[-1])  oxirgi indeksdagi element

# ro'yxatni oxiridan qo'shish
# aralash.append('baliq')
# aralash.append('anor')
# aralash.append('mashina')
# print(aralash)


# ro'yxatni xoxlagan joyiga yangi malumot qo'shish
# aralash.insert(3, 'nexia')
# aralash.insert(5, 'radio')
# print(aralash)



# aralash = ['kitob', '34', '20','Quyosh' ,'alifbo', '0', 'havo']

# print(aralash)
# ro'yxat elementini o'chirish
# del aralash[1]
# del aralash[3]
# del aralash

# aralash.remove(20)

# print(aralash)
# ro'yxat ichidan elementlarni sug'urib olish
# soz = aralash.pop(3)

# print(aralash)
# print(soz)


# bo'sj ro'yxat yaratish va uni to'ldirish
# cars = []

# cars.append('Cobalt')
# cars.append('Nexia')
# cars.append('Damas')

# print(cars)

# Amaliyot uchun mashq
#1 ismlar degan bo'sh ro'yxat yaratilsin va append va insert yordamida 3, 4 ta
# ism kiritilsin

# har bir ismga xabar print qilinsin: Salom Ali
# Salom Vali

# ismlar = []

# ismlar.append('Ali')
# ismlar.append('Vali')

# ismlar.insert(1, 'Hasan')
# ismlar.insert(1, 'Husan')

# print(ismlar)

# print(f"Salom {ismlar[0]}")
# print('Salom', ismlar[1])
# print('Salom '+ ismlar[2])
# print('Salom', ismlar[3])


#2 sonlar royxati yaratilsin va musbat manfiy sonlar kiritilsin
# 1 + 3
# 2 - 1
# 5 * 3
# 4 / 5

# sonlar = [1,23,54,-1,-34,-2,45,67,56,-34]
# print(sonlar[1] + sonlar[3])
# print(sonlar[2] - sonlar[1])
# print(sonlar[5] * sonlar[3])
# print(sonlar[4] / sonlar[5])


# Ro'yxat elementlari bilan ishlash

# cars = ['nexia', 'damas', 'cobalt', 'captiva', 'matiz', 'Spark', 'Malibu']

# tarkibini o'zgartigan holatda tartiblaydi sort()
# cars.sort(reverse=True)

# sonlar = [64,23,4,6, 12, 54, 2]
# a = sonlar.sort()
# print(sonlar)
# print(a)
# print(sonlar)
# print(cars)


# tarkibini o'zgartirmagan holatda tartiblash
# print(sorted(cars))
# print(cars)

# tartiblab teskari o'girib qo'yadi
# print(sorted(cars, reverse=True))

# O'z holatida teskari o'girib qo'yadi (ro'yxatni tarkibini o'zgartiradi)
# cars.reverse()

# print(cars)


# cars = ['nexia', 'damas', 'cobalt', 'captiva', 'matiz', 'Spark', 'Malibu', 'audi']

# ro'yxat uzunligi yoki ichida nechta element borligi len()
# print(len(cars))


# aralash = ['kitob', '34', '20','Quyosh' ,'alifbo', '0', 'havo']

# aralash.sort()
# print(aralash)


# sonlar = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# range() --> sonlar ketma-ketligini yaratadi

# numbers = list(range(1, 21))
# numbers = list(range(30)) # agar birinchi qiymat berilmasa nol dan boshlaydi
# list() sonlar ketma ketligini ro'yxat shakliga keltiryabti
# numbers = list(range(1, 40, 2)) toq sonlar
# numbers = list(range(2, 21, 2)) juft sonlar
# numbers = list(range(2, 21, 5))

# print(numbers)


# sonli ro'yxat amallari

# sonlar = list(range(1, 31))
# print(sonlar)
 
# print(max(sonlar)) # sonlar royxati ichidagi eng katta son
# print(min(sonlar))# sonlar royxati ichidagi eng kichik son
# print(sum(sonlar)) # sonlar royxati ichidagi barcha sonlar yig'indisi



# sozlar = ['olma', 'kitob', 'shahar', 'havo', 'suv', 'anor']

# yangi_sozlar = sozlar[2:5]
# yangi_sozlar = sozlar[:4] # boshidan boshlab oladi
# yangi_sozlar = sozlar[1:] # oxirigacha oladi
# yangi_sozlar = sozlar[:] # to'liq ko'chirib oladi
# yangi_sozlar[1] = 'aaa'

# print(sozlar)
# print(yangi_sozlar)


# UYGA VAZIFA

# 1. davlatlar ro'yxati yaratilsin, sort(), reverse(), sorted()

# 2. 100 dan 1000 gacha bo'lgan juft sonlar royxati yaratasizlar
# yigindisini toping
# 100 dan 1000 gacha nechta son borligini toping
# shu royxat boshidan 20 ta o'rtasidan 20 ta va oxiridan 20 ta sonlarni alohida
# ro'yxatga oling




# 3. taomlar degan ro'yxat yararilsin kamida 6,7 ta taom kiritilsin
# nonushta degan o'zgaruvchi taomlardan nusxa olinsin\
# natija print qilinsin



sonlar = list(range(100,1000,2))
sonlar1 = sonlar[:20]
sonlar2 = sonlar[215:235]
sonlar3 = sonlar[-20:]
print(sonlar1)
print(sonlar2)
print(sonlar3)
print(sum(sonlar))
print(len(sonlar))




