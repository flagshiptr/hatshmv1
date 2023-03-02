giris = """
7777    777777777777777777777777777777777777777777  
7777    7777        777      77     77
77777777777777777777777      77     7777777777
7777    7777        777      77            77
7777    7777        777      77  77777777777

        Coded By Ahlaksız Coder    *************
                   FlagShip
Hats Hesap Makinesi    >> İnstagram @ahlaksizcoder <<
"""
print(giris)
sayi1 = float(input('1. Sayıyı Giriniz >>'))
sayi2 = float(input('2. Sayıyı Giriniz >>'))

islem = input('İşlemi Giriniz (+,-,*,/) >>')

if islem == '+':
    sonuc = sayi1 + sayi2
    print('=============================')
    print(sonuc)
    print('=============================')
elif islem == '-':
    sonuc = sayi1 - sayi2
    print('=============================')
    print(sonuc)
    print('=============================')
elif islem == '*':
    sonuc = sayi1 * sayi2
    print('=============================')
    print(sonuc)
    print('=============================')
elif islem == '/':
    sonuc = sayi1 / sayi2
    print('=============================')
    print(sonuc)
    print('=============================')
else:
    print('Hatalı Giriş, Tekrar Deneyiniz..')




