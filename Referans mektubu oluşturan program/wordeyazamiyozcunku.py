#Varsayalım ki kullanıcıdan aldığı bilgiler doğrultusunda, özel bir konu üzerine
#referans mektubu oluşturan bir program yazmak istiyorsunuz. Referans mektubu
#taslağı aşağıda belirtildiği gibi olsun. Amacınız bu dilekçedeki boşluklara gelmesi
#gereken bilgileri kullanıcıdan alıp, eksiksiz bir dilekçe ortaya çıkarmak.
#Kullanıcıdan bilgileri input() fonksiyonu ile alıp metinde yerlerine kaçış dizilerini
#kullanarak print() fonksiyonu içerisinde kullanılan format metodu yardımıyla ekrana
#yazdırınız




# Mektup değişkenini değişecek konumları indis değerleri ile belirterek oluşturduk
mektup = ("""

                                                                                  Tarih: {}
                       {} Programı
                       {} Başvurusu 
                       Referans Mektubu
{} Üniversitesi	{} programı öğrencisi olan {}'ya 2022-2023 güz eğitim
öğretim yılında {} dersi tarafımdan verilmiştir.
{}'nunun iş başvurusu kabul edildiği takdirde başarılı bir çalışan olacağını düşündüğümü
belirtmek isterim.

Saygılarımla.
Telefon : {}
E-posta : {}


                                                                                  Öğr.Gör {}
                                                                                 {} Üniversitesi 
	                                                                              {} Bölümü




""")

# kullanıcıya iletilecek ilk çıktı
print("""Bu program hızlıca referans mektubu oluşturmanız için tasarlanmıştır. 
aşağıdaki bilgileri girerek dilekçenizi oluşturabilirsiniz.

Evet word ile yapsak daha mantıklı ama bizde böyle seviyoz

""")

# kullanıcıdan alınan değerler
tarih = input("Dilekçe tarihini giriniz > ")
program = input("Programınızı giriniz > ")
basvuru = input("Basvuru tipini giriniz > ")
universite = input(" Üniversite adını giriniz > ")
ograd = input("Öğrenci adını giriniz > ")
ders = input("Alınan dersi giriniz > ")
telefon = input("Telefon numarasını giriniz > ")
posta = input("E postanızı giriniz > ")
ogrgor = input("Öğretim görevlisinin adını giriniz > ")

# format yardımı ile ilgili indis boşluklarına kullanıcıdan aldığımız değerleri yerleştirdik
print(mektup.format(tarih, program, basvuru, universite,
program, ograd, ders,
ograd, telefon, posta,
ogrgor, universite, program))

# daha az uykumun olduğu bir süreçte worde düzgün bir formatta yazdıracak şekilde düzenleyeceğim bunu
