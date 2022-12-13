# UYGA VAZIFA KODI

# for x in range(1,6):
#     for i in range(1,x+1):
#         print('*',end=' ')
#     print(' ')
# m = 5
# for a in range(1,6):
#     for j in range(m-a,0,-1):
#         print('*',end=' ')
#     print(' ')

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


# IF ELSE

son = 15

# if son > 10:
#     print('Kattaroq son ekan')
# else:
#     print('Son kichikroq ekan')

# shart to'g'ri bo'lsa if ni tarkibidagi kod bajariladi
# shart xato bo'ls else ni tarkibidagi kod bajariladi
# if son == 15:
#     print('15-xona')
# else:
#     print('Boshqa xona')

# soz = 'Rossiya'

# if soz == 'Rossiya':
#     print('Rossiyaga xush kelibsiz')
# else:
#     print('Boshqa davlat')


# if ni matnl ichida birorta so'z yoki ro'yxat ichida birorta element borligini tekshirish uchun ishlatish

# matn = 'Rossiya imperiyasi 1865-yilda Toshkentni, 1876-yilda Qoʻqonni magʻlub etdi. Rossiya fuqarolar\
#      urushidan keyin togʻlarda bolsheviklarga boʻlinib ketgan qarshilik 1930-yillargacha davom etdi.\
#          1919-yilda Rossiyaga boʻysungan Buxoro va Xiva amirliklari agʻdarilib, keyingi yili Buxoro\
#              Xalq Respublikasi va Xorazm Xalq Respublikasidan nominal mustaqillikka erishdilar. \
#                 1924-yilda Buxoro va Xorazm Xalq respublikalari, sobiq Qoʻqon tarkibiga kiruvchi \
#                     Oʻzbekiston Sovet Sotsialistik Respublikasi tuzildi. Sovet Ittifoqi Oʻzbekistonni \
#                         paxtachilik hududiga aylantirdi va qishloq xoʻjaligini qayta qurishning taʼsiri\
#                              hozir ham mamlakatda sezilmoqda'


# if 'kitob' in matn:
#     print('Bu soz bor ekan')
# else:
#     print('Bu soz yoq ekan')



# cars = ['nexia', 'lacetti' ,'damas', 'cobalt', 'malibu']
# mashina = 'lacetti'

# if mashina in cars:
#     print('Sotib olishingiz mumkin')
# else:
#     print('Bu mashinadan bizda yoq')

# cars = ['nexia', 'lacetti' ,'damas', 'bmw' ,'cobalt', 'malibu']


# for i in cars:
#     if i == 'bmw':
#         print(i.upper())
#     else:
#         print(i.title())




# parol = input('Parolni kiriting: ')
# if len(parol)<5:
#     print('Sizni parolingiz xato formatda')

# else:
#     print('Parol saqlandi')


# ism = input('Ism kiriting')

# ismlar = ['ali', 'vali','hasan']

# if ism in ismlar:
#     print('Siz qabul qilindingiz')
# else:
    # print('Qabul qilinmadingiz')

# AMALIYOT
# cars = ['totota', 'mazda', 'hyundai', 'gm', 'kia']


# for i in cars:
#     if i != 'gm':
#         print(i.title())
#     else:
#         print(i.upper())
# for i in cars:
#     if i == "gm":
#         print(i.upper())
#     else:
#         print(i.title())



# ismlar = ['ali', 'vali','hasan']

# if 'ali' not in ismlar: # ali ismlar royxati ichida BO'LMASA
#     print('Siz qabul qilinmadingiz')
# else:  # ali ismlar royxati ichida BO'LSA
#     print('Qabul qilinmadingiz')


# login = input('Loginni kiriting: ')

# if login == 'admin':
#     print('Admin xush kelibsiz')
# else:
#     print(login)


# son1 = int(input('Birinchi sonni kiriting: '))
# son2 = int(input('Ikkinchi sonni kiriting'))

# if son1 == son2:
#     print('Sonlar teng')
# else: 
#     print('Sonlar teng emas')



# Foydalanuvchidan son kiritishini so'raysizlar,
#agar son manfiy bo'lsa 'son manfiy'
#  agar son son musbat bo'lsa 'son musbat' 
# son = int(input("Sonni kiriting\n"))

# if son > 0:
#     print('Son musbat')
# elif son < 0:
#     print('Manfiy')
# else:
#     print('Nol')



# yosh = int(input('Yoshingizni kiriting: '))
# tugilgan yilingizni kiriting 
# yosh --> ?

# if yosh<10:
#     print('5000 sum')
# elif yosh < 18:
#     print('10000 sum')
# elif yosh < 24:
#     print('15000 sum')
# else:
#     print('20000 sum')

# 24 dan katta bolsayu va 60 dan kichik bo'lsa 20000 sum, 60dan kattalarga bepul bolsin

# yil = int(input("Tug'ilgan yilingizni kiriting\n"))

# yosh = 2022-yil  

# if yosh < 10:
#     print("5000 so'm")
# elif yosh < 18:
#     print("10000 so'm")
# elif yosh < 24:
#     print("15000 so'm")
# elif yosh < 60:
#     print("20000 so'm")
# else:
#     print("Sizga kirish bepul")




# yil = int(input("Tug'ilgan yilingizni kiriting\n"))

# yosh = 2022-yil  

# narx = ''

# if yosh < 10:
#     narx = '5000 sum'
# elif yosh < 18:
#     narx = '10000sum'
# elif yosh < 24:
#     narx = '15000sum'
# elif yosh < 60:
#     narx = '20000sum'
# else:
#     narx = '0 sum'


# print('Sizga kirish narxi', narx)




# kun = input('Bugungi hafta kunini kiriting: ')

# if kun == 'shanba' or kun == 'yakshanba': # or - yoki, bu bir nechta shartlardan 1 tasi togri bolsa ham true qaytaradi
#     print('Dam olish')
# else:
#     print('Ish kuni')


# kun = input('Bugungi hafta kunini kiriting: ')
# havo = 30
# if kun == 'yakshanba' and havo > 35  : # and - va; Bu birt nechta shartlarni hammasi togri bolsa true qaytaradi 
#     print('Chumilishga boramiz')
# else:
#     print('Bormaymiz')



# menyu = ['osh', 'manti', 'kabob', 'gril']

# buyurtmalar = ['osh', 'somsa', 'kabob']

# for i in buyurtmalar:
#     if i in menyu:
#         print(f"{i} buyurtma qildingiz")
#     else:
#         print(f'{i} menyuda yoq')


# mevalar = [3,4,323]

# if len(mevalar) == 0:
#     print('Bosh')
# else:
#     print('Bosh emas')

# if mevalar:
#     print('Bosh emas ekan')
# else:
#     print('Bosh ekan')


# 15 ni 5 ga qoldiqsiz bo'linishini tekshirish

# if 120%5 == 0:
#     print('Son 5 ga bolinadi')
# else:
#     print('Bolinmaydi')


# son kiritilsin, shu son juft yoki toqligi tekshiradigan kod yozing
# son = int(input('Sonni kiriting\n'))
# if son%2 == 0:
#     print("Bu son juft")
# else:
#     print("Bu son toq")


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan 
# bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['non', 'olma', 'sabzi', 'kalbasa', 'nok', 'sut']

# savat = []

# for i in range(1, 6):
#     s = input(f"{i} - mahsulotni kiriting: ")
#     savat.append(s)


# for i in savat:
#     if i in mahsulotlar:
#         print('Mahsulot dokonimizda bor')
#     else:
#         print('Mahsulot dokonimizda yoq')


# UYGA VAZIFA
#1-vazifa

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


# 2-vazifa

#Foydalanuvchidan biror butun son kiritishni so'rang. misol uchun 240 . Foydalanuvchi kiritgan sonni 
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

# 240 - 2 ga bolinadi
# 240 - 3 ga bolinmaydi
# 240 - 4 ga bolinadi
# 240 - 5 ga bolinadi
# .
# .
# .
# .
# 240 - 10 ga bolinadi






