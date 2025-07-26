import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifrenizin uzunluğunu girin: "))
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakterler)
print("Oluşturulan şifre:", sifre)
