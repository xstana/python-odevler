#Telefon, Radyo, TV, Kamera, Saat gibi bir elektronik eşyayı aklımızdan tutalım.
#Bilgisayarda bu elektronik nesneyi, aşağıdaki karar ağacına benzer ya da aynı şeklinde
#bir karar ağacını kodlayarak bulunuz.


# Boolean olarak çeeşitli değişken koşulları ve özellikleri belirttik
database = [
    {"secenek":"Telefon", "goruntu":True, "tasinir":True, "arama":True , "cekim":False, "anten":False, "kol":False},

    {"secenek": "Radyo", "goruntu": False, "tasinir": True, "arama": False, "cekim": False, "anten": True,"kol": False},

    {"secenek": "Televizyon", "goruntu": True, "tasinir": False, "arama": False, "cekim": False, "anten": False,"kol": False},

    {"secenek": "Kamera", "goruntu": True, "tasinir": True, "arama": False, "cekim": True, "anten": False,"kol": False},

    {"secenek": "Saat", "goruntu": False, "tasinir": True, "arama": False, "cekim": False, "anten": False,"kol": True},

]


#kullanıcının karşılaşacağı ilk çıktı ve yönlendirmeler
print(""" 

Kahiython'a hoş geldin!

Aklından aşağıda bulunan eşyalardan birini tut daha sonra sana sorduğum sorular ile bunu bulmaya çalışacağım!

* Telefon
* Radyo
* Televizyon
* Kamera 
* Saat (akıllı değil gerizekalı saat)

Hazır olduğunda başlamak için enter'a bas!

""")
input()

print(""" 
Sana soracağım soruları evet ve hayır şeklinde yanıtlamalısın! 

Evet için e hayır için h seçeneğini kullanabilirsin!

Devam etmek için enter'a bas!

""")
input()

# İhtimal olarak hesabı yapan fonksiyonumuz gerekli hesaplamayı yapıp soruları bu doğrultuda özelleştirecek ve minimum soru ile cevabı bulmamızı sağlayacak
def ihtimal(answer, property):
    if answer == "e":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("BULDUM ! Seçtiğin şey bir "+database[0]["secenek"])
        quit()

# Sorularımız ve e durumunda true konumuna alacağı özellik
        
ans = input("Bu eşyadan bir şeyler izleyebilirmisin? (e,h)")
ihtimal(ans, "goruntu")

ans = input("Bu şeyi kolaylıkla yanında taşıyabilirmisin?(e,h)")
ihtimal(ans, "tasinir")

ans = input("Bu şey arama yapabilir mi? (e,h)")
ihtimal(ans,"arama")

ans = input("Bu şey fotoğraf çekebilir mi?(e,h)")
ihtimal(ans,"cekim")

ans = input("Seçtiğin şeyin anteni var ve müzik mi çalıyor ?(e,h)")
ihtimal(ans,"anten")

ans = input("Seçtiğin şey kola mı takılıyor? (e,h)")
ihtimal(ans,"kol")
