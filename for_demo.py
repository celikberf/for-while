sayilar = [1,3,5,7,9,12,19,21]

#1- Sayilar listesindeki hangi sayılar 3'ün katıdır ? 
for sayi in sayilar:
    if sayi %3 == 0:
        print(sayi)

#2- Sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0

for sayi in sayilar:
    toplam  += sayi
    print(toplam)

#3- Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if sayi %2 != 0:
        kare = sayi ** 2
        print(kare)

sehirler = ['kocaeli', 'istanbul' , 'ankara', 'izmir', 'rize']

#Şehirlerrden hangileri en fazla 5 karakterlidir ? 

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)


urunler = [
    {'name' : 'samsung S6', 'price' : '3000'},
    {'name' : 'samsung S7', 'price' : '4000'},
    {'name' : 'samsung S8', 'price' : '5000'},
    {'name' : 'samsung S9', 'price' : '6000'},
    {'name' : 'samsung S10', 'price' : '7000'}

]

#5- Ürünlerin fiyatların toplamı nedir ? 
# toplam = 0

# for urun in urunler:
#     toplam += int(urun['price'])
#     print(toplam)

#6- Ürünlerdeen fiyatı en fazla 5000 olan ürünleri gösteriniz. 

for urun in urunler:
    if int(urun['price']) <= int(5000):
        print(f"Ürün Adı : {urun['name']} Fiyat : {urun['price']}")