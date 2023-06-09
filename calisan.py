
from insan import insan
class calisan(insan):
    # istenilen değerleri bulunduran init metodunu yazıyoruz
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas=None):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        sektor_liste = ["teknoloji", "muhasebe", "insaat", "diger"]
        #nesneye girilen sektör değerinin geçerli değerleden biri olması için while döngüsüyle kontrol ediyoruz ve hatalıysa tekrar girmesini istiyoruz
        while self.__sektor not in sektor_liste:
            self.__sektor = input("lütfen sektör değerini inşaat, muhasebe, teknoloji veya diğer olarak girin:")
        self.__tecrube = tecrube
        self.__maas = maas
        if yeni_maas is None:
            self.__yeni_maas = yeni_maas

    # private değerleri getirip değiştirmek için get-set metodları yazdık
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor_deger):
        sektor_liste = ["teknoloji", "muhasebe", "insaat", "diger"]
        while sektor_deger not in sektor_liste:
            sektor_deger = input("lütfen sektör değerini inşaat, muhasebe, teknoloji veya diğer olarak girin:")
        self.__sektor = sektor_deger

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, yeni_tecrube):
        self.__tecrube = yeni_tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_yeni_maas):
        self.__yeni_maas = yeni_yeni_maas

    #yeni maaş değerini hesaplamak için zam hakki metodunu yazıyoruz
    def zam_hakki(self):
        #tecrube ve maas değerlerini bizden istenilen şekilde karşılaştırıp yeni maaş değeri buluyoruz
        if self.__tecrube / 12 < 2:
            zam_orani = 0
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        elif self.__tecrube / 12 >= 2 and self.__tecrube < 4 and self.__maas < 15000:
            zam_orani = self.__maas % self.__tecrube
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        elif self.__tecrube / 12 >= 4 and self.__maas < 25000:
            zam_orani = (self.__maas % self.__tecrube) / 2
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        else:
            self.__yeni_maas = self.__maas

    #istenilen değerleri string haline getiriyoruz str ile
    def __str__(self):
        self.zam_hakki()
        return f"AD: {self.get_ad()}, SOYAD: {self.get_soyad()}, TECRUBE: {self.get_tecrube()} AY, YENI MAAS: {self.get_yeni_maas()}"




