#sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar listesini while ile ekrana yazdırın

"""
x = 1 
while x < len(sayilar):
    print(sayilar[x])
    x += 1

"""

#2- Başlangıc ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır

"""
baslangic = int(input('baslangıç sayısı : '))
bitis = int(input('bitiş sayısı : '))

sayi = baslangic

while sayi < bitis: 
        sayi += 1
        if sayi % 2 == 1:
            print(sayi)
"""
#3- 1-100 sayıları azalan şekilde yazdırın
"""
x = 100

while x > 0:
      print(x)
      x -=1
"""

#4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdır

"""
sayilar = []
i = 0
while i < 5 :
    sayi = int(input(f"{i+1}. sayıyı girin : "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
print('Girilen sayılar bk sırayla : ' , sayilar)

"""
#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
# ** ürün sayısını kullanıcıya sorun
# ** distionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

"""
urunler = []

urunSayisi = int(input('kaç ürün olacak : '))

i = 0 

while i < urunSayisi:
    name = input(f"{i+1}. ürünün ismini giriniz : ")
    price = float(input(f"{i+1}. ürünün fiyatını giriniz :  "))
    urunler.append({'name' : name , 'price' : price})
    i+=1
    
print("Eklenen ürünler : ")

i = 0 

while i < len(urunler):
    print(f'Ürünün adı : {urunler[i]['name']}, Fiyat : {urunler[i]['price']}')
    i+=1

"""