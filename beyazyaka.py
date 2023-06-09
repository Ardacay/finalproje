from calisan import calisan
class beyazyaka(calisan):
    # istenilen değerleri bulunduran init metodunu yazıyoruz
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, tesvik_primi):
        # Insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyoruz
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__tesvik_primi = tesvik_primi
        # istediğimiz aralıkta tesvik primi değeri girilmesi için while döngüsüyle kontrol edip hatalı değerde tekrar girilmesini sağlıyoruz
        while self.__tesvik_primi < 100:
            self.__tesvik_primi = int(input("Lütfen 100'den büyük bir teşvik primi değeri girin:"))

    # private değerleri getirip değiştirmek için get-set metodları yazdık
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, yeni_tesvik_primi):
        while yeni_tesvik_primi < 100:
            yeni_tesvik_primi = int(input("Lütfen 100'den büyük bir teşvik primi değeri girin:"))
        self.__tesvik_primi = yeni_tesvik_primi

    # yeni maaş değerini hesaplamak için zam hakki metodunu yazıyoruz
    def zam_hakki(self):
        # tecrube ve maas değerlerini bizden istenilen şekilde karşılaştırıp teşvik primi değerini de kullanarak yeni maaş değeri buluyoruz
        if self.get_tecrube() / 12 < 2:
            zam_orani = self.get_tesvik_primi() * 10
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))
        elif self.get_tecrube() / 12 >= 2 and self.get_tecrube() < 4 and self.get_maas() < 15000:
            zam_orani = (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            self.set_yeni_maas(self.get_maas() + zam_orani)
        elif self.get_tecrube() / 12 >= 4 and self.get_maas() < 25000:
            zam_orani = (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            self.set_yeni_maas(self.get_maas() + zam_orani)
        else:
            self.set_yeni_maas(self.get_maas())
    #istenilen değerleri string haline getiriyoruz str ile
    def __str__(self):
        self.zam_hakki()
        return f"AD: {self.get_ad()}, SOYAD: {self.get_soyad()}, TECRUBE(AY): {self.get_tecrube()} AY, YENI MAAS: {self.get_yeni_maas()}"