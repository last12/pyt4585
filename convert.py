# convert elinizdeki veri tipini farkli bir tipe cevirmeye yarar


# int() : tam sayi  veri tipine  cevirir
# str() : string(metinsel) degere cevirme islemi yapar
# float()  : ondalikli degere cevirme islemi yapar
# chr() : verdiginiz  sayisal degerin karakter karsiligini teslim eder
# ord() : verdiginiz karakterin , ascii (sayisal) karsiligini teslim eder

# print (sayi1)
# print (type(sayi1))


# print (sayi1+sayi2)

# ctrl + k + c => yorum satiri alir
# crtl + k + u => yorum satirindan alir
# alt + shift + f => kodlari duzenle

# toplam = float (sayi1) + float(sayi2)
# print(toplam)
# result = int(sayi1) + int(sayi2)
# print(result)


sayi1 = input("lutfen 1. sayiyi giriniz : ")
sayi2 = input ("lutfen 2. sayiyi giriniz : ")

print(sayi1)
print(type(sayi1))


print(chr(65),ord('A'))
print(chr(90),ord('Z'))
print(chr(97),ord('a'))
print(chr(122),ord('z'))

sayi = 100

print("sayinin degeri",sayi)
print("sayinin degeri " +str(sayi))