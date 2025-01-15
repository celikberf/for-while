numbers = [1,2,3,4,5]

for num in numbers: # listenin içerisinden tek tek elemanları al 'num' içine at ve her for döndüğünde elemanları ekrana yazdır
    print(num)

names = ['berfin', 'güler', 'soner']

for name in names:
    print(f'my name is {name}') # my name is berfn , my name is güler , my name is soner

name = 'berfin'

for n in name: # her karakteri alt alta tek tek yazdırır . b e r f i n
    print(n)

tuple = [(1,2),(3,4),(5,6)]

for t in tuple:
    print(t)

d = {'k1' : 1 , 'k2' : 2 , 'k3' : 3}

for key,value in d.items(): # hem key hem value elemanlarına ulaaşırız.
    print(key,value)