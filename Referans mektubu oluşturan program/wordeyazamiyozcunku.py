
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

print("""Bu program hızlıca referans mektubu oluşturmanız için tasarlanmıştır. 
aşağıdaki bilgileri girerek dilekçenizi oluşturabilirsiniz.

Evet word ile yapsak daha mantıklı ama bizde böyle seviyoz

""")


tarih = input("Dilekçe tarihini giriniz > ")
program = input("Programınızı giriniz > ")
basvuru = input("Basvuru tipini giriniz > ")
universite = input(" Üniversite adını giriniz > ")
ograd = input("Öğrenci adını giriniz > ")
ders = input("Alınan dersi giriniz > ")
telefon = input("Telefon numarasını giriniz > ")
posta = input("E postanızı giriniz > ")
ogrgor = input("Öğretim görevlisinin adını giriniz > ")

print(mektup.format(tarih, program, basvuru, universite,
program, ograd, ders,
ograd, telefon, posta,
ogrgor, universite, program))

