# 1-100 e kadar



"""
x = 1

while x <= 100:
    if x % 2 == 1:
        print(f'sayi tek : {x}')

    else : 
        print(f'sayı çift : {x}')
    x += 1

"""

name = '' # False
while not name.strip(): # .strip => kullanıcı 'bosluk' karakteri girerse , tekrar isim girmeyi isticek
    name = input('isminizi giriniz : ')

print(f'Merhaba , {name}') # isim girmediğimiz sürece , girmemizi isteyecek.
