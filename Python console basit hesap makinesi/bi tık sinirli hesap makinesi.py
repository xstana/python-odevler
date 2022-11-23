print("""********************************

 * Agresif hesap makinesi 1.0

Yapmak istediğiniz işlemi tuşlayınız

1 > Toplama
2 > Çıkarma
3 > Çarpma
4 > Bölme
 
****************************************
""")
while True:
    islem = input("İşlem Seçiniz (Çıkış için 'q'): ")
    if islem == 'q':
        quit()
    elif islem == "1":
        print("+  ------Toplama İşlemi------  +")
        sayi1 = int(input("1.Sayıyı Giriniz: "))
        sayi2 = int(input("2.Sayıyı Giriniz: "))
        print("{}  +   {}    =  {}".format(sayi1, sayi2, sayi1+sayi2))

    elif islem == "2":
        print("-  -----Çıkarma İşlemi-----  -")
        sayi1 = float(input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{}  -   {}    =  {}".format(sayi1, sayi2, sayi1-sayi2))
    elif islem == "3":
        print("*  ------Çarpma İşlemi------  *")
        sayi1 = float(input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))


    elif islem == "4":
        print(" / ------Bölme İşlemi------ /")
        try:
            sayi1 = int(input("1.Sayıyı Giriniz: "))
            sayi2 = int(input("2.Sayıyı Giriniz: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        except ZeroDivisionError:
            print("Sence bir sayıyı sıfıra bölebilirmisin bebis?")
        except ValueError:
            print("Hayat hikayeni değil sayı gir kardeşim")
    else:
        print("1 var 2 var 3 var 4 var ne seçiyon güzel kardeşim??")
