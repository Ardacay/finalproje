#modülleri import ediyoruz
from insan import insan
from issiz import issiz
from calisan import calisan
from mavviyaka import mavviyaka
from beyazyaka import beyazyaka
import pandas as pd
#dataframe de  görüntülenen maksimum sütün saysını arttırıyoruz
pd.set_option("display.max_columns", 15)
#örneklerini girip ekrana yazdırıyoruz
kisi_1 = insan(tc_no=64973,ad="arda",soyad="kaya",yas=34,cinsiyet="erkek",uyruk="türk")
kisi_2 = insan(tc_no=84621,ad="mustafa",soyad="yas",yas=24,cinsiyet="erkek",uyruk="alman")

print(kisi_1.__str__(),"\n",kisi_2.__str__(),"\n")

kisi_3 = issiz(tc_no=16759,ad="serkan",soyad="bakır",yas=32,cinsiyet="erkek",uyruk="türk",mavi_yaka=5,beyaz_yaka=8,yonetici=10)
kisi_4 = issiz(tc_no=78963,ad="ömer",soyad="bugra",yas=45,cinsiyet="erkek",uyruk="türk",mavi_yaka=0,beyaz_yaka=4,yonetici=3)
kisi_5 = issiz(tc_no=76412,ad="aslı",soyad="kartal",yas=38,cinsiyet="kadın",uyruk="türk",mavi_yaka=9,beyaz_yaka=3,yonetici=0)

print(kisi_3.__str__(),"\n",kisi_4.__str__(),"\n",kisi_5.__str__(),"\n")

kisi_6 = calisan(tc_no=94673,ad="ayşe",soyad="kurt",yas=44,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=78,maas=40000,yeni_maas=0)
kisi_7 = calisan(tc_no=14734,ad="ahmet",soyad="karahan",yas=54,cinsiyet="erkek",uyruk="rus",sektor="insaat",tecrube=98,maas=10000,yeni_maas=0)
kisi_8 = calisan(tc_no=51675,ad="ercüment",soyad="cözer",yas=24,cinsiyet="kadın",uyruk="türk",sektor="muhasebe",tecrube=36,maas=16000,yeni_maas=0)

print(kisi_6.__str__(),"\n",kisi_7.__str__(),"\n",kisi_8.__str__(),"\n")

kisi_9 = mavviyaka(tc_no=12345,ad="yusuf",soyad="cay",yas=64,cinsiyet="erkek",uyruk="türk",sektor="teknoloji",tecrube=67,maas=23000,yeni_maas=0,yipranma_payi=0.6)
kisi_10 = mavviyaka(tc_no=22189,ad="ayça",soyad="yirmiiki",yas=58,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=37,maas=16000,yeni_maas=0,yipranma_payi=0.3)
kisi_11 = mavviyaka(tc_no=67428,ad="muharrem",soyad="keskin",yas=44,cinsiyet="erkek",uyruk="alman",sektor="diger",tecrube=25,maas=13000,yeni_maas=0,yipranma_payi=0.8)

print(kisi_9.__str__(),"\n",kisi_10.__str__(),"\n",kisi_11.__str__(),"\n")

kisi_12 = beyazyaka(tc_no=94651,ad="melis",soyad="kızıl",yas=33,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=28,maas=43000,yeni_maas=0,tesvik_primi=500)
kisi_13 = beyazyaka(tc_no=36475,ad="muahmmed",soyad="kayık",yas=59,cinsiyet="erkek",uyruk="yunan",sektor="insaat",tecrube=50,maas=13000,yeni_maas=0,tesvik_primi=600)
kisi_14 = beyazyaka(tc_no=17943,ad="taner",soyad="tarlacı",yas=64,cinsiyet="erkek",uyruk="türk",sektor="muhasebe",tecrube=46,maas=22000,yeni_maas=0,tesvik_primi=250)

print(kisi_12.__str__(),"\n",kisi_13.__str__(),"\n",kisi_14.__str__(),"\n")
#dataframede kullanacağımız nesneleri listeye atıyoruz
nesneler = [kisi_6,kisi_7,kisi_8,kisi_9,kisi_10,kisi_11,kisi_12,kisi_13,kisi_14,]
#dataframe oluşturmak için kullanacağımız dicti oluşturuyoruz
sözlük = {"tc_no": [], "ad": [], "soyad": [], "yas": [], "cinsiyet": [], "uyruk": [], "sektor": [], "tecrube(ay)": [], "maas": [],"yeni maas": [] ,"yıpranma_payi": [], "tesvik_primi": [],"çalışan_tipi": []}
#nesneler listesindeki  nesneler için  for döngüsünü oluşturuyoruz
for nesne in nesneler:
    #nesnenin yeni maaş değerinin hesaplanması için zam hakki metodu çağırıyoruz
    nesne.zam_hakki()
    #her bir nesnenin değerlerini dicte kaydediyoruz
    sözlük["tc_no"].append(nesne.get_tc_no())
    sözlük["ad"].append(nesne.get_ad())
    sözlük["soyad"].append(nesne.get_soyad())
    sözlük["yas"].append(nesne.get_yas())
    sözlük["cinsiyet"].append(nesne.get_cinsiyet())
    sözlük["uyruk"].append(nesne.get_uyruk())
    sözlük["sektor"].append(nesne.get_sektor())
    sözlük["tecrube(ay)"].append(nesne.get_tecrube())
    sözlük["maas"].append(nesne.get_maas())
    sözlük["yeni maas"].append(nesne.get_yeni_maas())
    sözlük["çalışan_tipi"].append(type(nesne).__name__)
    #istenilen değerin nesnede bulnmaması haline try-except kullanarak sözlükte o değerlerin None değerini almasını sağlıyoruz
    try:
        sözlük["yıpranma_payi"].append(nesne.get_yipranma_payi())
    except AttributeError:
        sözlük["yıpranma_payi"].append(None)
    try:
        sözlük["tesvik_primi"].append(nesne.get_tesvik_primi())
    except AttributeError:
        sözlük["tesvik_primi"].append(None)
#pandas modülünü kullanarak dictionary'den dataframe oluşturuyoruz ve ekrana yazdırıyoruz
df = pd.DataFrame(sözlük).fillna(0)
print(df)


#shape metodu kullanarak maaşı 15000 den fazla olanları yazdırıyoruz
maas__15000__uzeri = df[df["maas"] > 15000].shape[0]
print("\nMaaşı 15000 TL üzerinde olanların toplam sayısı:", maas__15000__uzeri)
#dataframedeki değerleri çalışan tipine göre  her grubun ortalama maaş ve tecrübelerini ekrana yazdırıyoruz
gruplanmis_df = df.groupby("çalışan_tipi").agg({"yeni maas": "mean", "tecrube(ay)": "mean"})
print("\nÇalışan Tiplerine Göre Ortalama Maaş ve Tecrübe:")
print(gruplanmis_df)
#yeni maaş değerine df sıralıyoruz
sıralı_df = df.sort_values("yeni maas")
print("\nyeni maaş değerine göre sıralanmış dataframe:")
print(sıralı_df)
#ay halindeki tecrube değerini yıl ahline getirip 3 seneden fazla olan beyaz yakalıları yazdırıyoruz
print("\nTecrübesi 3 seneden fazla olan Beyaz yakalılar:")
filtre = (df["çalışan_tipi"] == "beyazyaka") & ((df["tecrube(ay)"]/12) >= 3)
print(df.loc[filtre])

print("\nYeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunları:")
filtre = (df['yeni maas'] > 10000) & (df.index > 2) & (df.index < 5)
print(df.loc[filtre, ['tc_no', 'yeni maas']])
#istenilen sütünlar alınıp yeni df oluşturuyoruz
print("\nyeni dataframe:")
yeni_df = df[["ad","soyad","sektor","yeni maas"]]
print(yeni_df)






