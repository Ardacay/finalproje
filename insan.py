#insan classı oluşturuyoruz
class insan:
    #istenilen özellikler bulunduran init metodunu yazıyoruz
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
    # private değerleri getirip değiştirmek için get-set metodları yazdık
    def get_tc_no(self):
        return self.__tc_no
    def set_tc_no(self,yeni_tc_no):
        self.__tc_no = yeni_tc_no

    def get_ad(self):
        return self.__ad
    def set_ad(self,yeni_ad):
        self.__ad = yeni_ad

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self,yeni_soyad):
        self.__soyad = yeni_soyad

    def get_yas(self):
        return self.__yas
    def set_yas(self,yeni_yas):
        self.__yas = yeni_yas

    def get_cinsiyet(self):
        return self.__cinsiyet
    def set_cinsiyet(self,yeni_cinsiyet):
        self.__cinsiyet = yeni_cinsiyet

    def get_uyruk(self):
        return self.__uyruk
    def set_uyruk(self,yeni_uyruk):
        self.__uyruk = yeni_uyruk
    #istenilen değerleri string haline getiriyoruz str ile
    def __str__(self):
        return f" TC:{self.__tc_no}, AD:{self.__ad}, SOYAD:{self.__soyad}, YAS:{self.__yas}, CİNSİYET:{self.__cinsiyet}, UYRUK:{self.__uyruk}"

