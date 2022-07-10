import math
import time

class Bilgisayar():
    def __init__(self, pc_durumu="Kapalı", isletim_sistemi=["Windows 10"], uygulamalar=["Google Chrome"],
                 baglı_cihazlar=["fare"]):
        self.pc_durumu=pc_durumu
        self.isletim_sistemi=isletim_sistemi
        self.uygulamalar=uygulamalar
        self.baglı_cihazlar=baglı_cihazlar

    def ac(self):
        if self.pc_durumu=="Açık":
            print("Bilgisayar Zaten Açık...")
        else:
            print("Bilgisayar Açılıyor...")
            time.sleep(1)
            self.pc_durumu="Açık"
            print("Bilgisayar Açıldı!")
    def kapat(self):
        if self.pc_durumu=="Kapalı":
            print("Bilgisayar Zaten Kapalı")
        else:
            print("Bilgisayar Kapatılıyor...")
            time.sleep(2)
            self.pc_durumu="Kapalı"
            print("Bilgisayar Kapandı!")
    def hesap_makinesi(self):
        if self.pc_durumu=="Açık":
            print("Hesap Makinesi Açılıyor...")
            time.sleep(2)
            print("""
            HESAP MAKİNESİNE HOŞGELDİNİZ!!!
            
            İŞLEMLER
            
            1-Toplama
            2-Çıkarma
            3-Çarpma
            4-Bölme
            5-Faktöriyel alma
            6-Karekök bulma
            7-Üs alma
            """)
            islem=input("Yapmak İstediğiniz İşlemi Giriniz: ")
            if islem=="1":
                sayi1=int(input("1. Sayı: "))
                sayi2=int(input("2. Sayı: "))
                print("Sonuç: ",sayi1+sayi2)
            elif islem=="2":
                sayi1 = int(input("1. Sayı: "))
                sayi2 = int(input("2. Sayı: "))
                print("Sonuç: ", sayi1-sayi2)
            elif islem=="3":
                sayi1 = float(input("1. Sayı: "))
                sayi2 = float(input("2. Sayı: "))
                print("Sonuç: ", sayi1*sayi2)
            elif islem=="4":
                try:
                    sayi1 = float(input("1. Sayı: "))
                    sayi2 = float(input("2. Sayı: "))
                    print("Sonuç: ", sayi1/sayi2)
                except ZeroDivisionError:
                    print("Paydaya 0'dan Başka Bir Sayı Giriniz!")
            elif islem=="5":
                sayi=int(input("Faktöriyeli Alınacak Sayı: "))
                print("{} Sayısının Faktöriyeli: {}".format(sayi,math.factorial(sayi)))
            elif islem=="6":
                sayi=int(input("Karekökü Bulunacak Sayı: "))
                print("{} Sayısının Karekökü: {}".format(sayi,math.sqrt(sayi)))
            elif islem=="7":
                sayi=int(input("Üssü Alanacak Sayı: "))
                üs=int(input("Üs sayısı: "))
                print("{} Sayısının {}. Üssü: {}".format(sayi,üs,math.pow(sayi,üs)))
            else:
                print("Geçersiz Komut!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def isletim_sistemi_ekle(self):
        if self.pc_durumu == "Açık":
            if self.isletim_sistemi==list():
                print("""
                İşletim Sisteminiz Bulunmamakta!
                
                YÜKLENEBİLECEK SİSTEMLER
                
                1-Windows 10
                2-Windows 11
                3-Linux
                4-Unix
                """)
                secim = input("Yüklemek İstediğiniz Sistemin Numarasını Giriniz: ")
                if secim == "1":
                    win10="Windows 10"
                    print("{} Sistemi Yükleniyor...\nLütfen Bekleyiniz...".format(win10))
                    time.sleep(3)
                    self.isletim_sistemi.append(win10)
                    print("{} Yüklendi! Bilgisayarı Yeniden Açmayı Unutmayın...".format(win10))
                    self.kapat()
                elif secim == "2":
                    win11="Windows 11"
                    print("{} Sistemi Yükleniyor...\nLütfen Bekleyiniz...".format(win11))
                    time.sleep(3)
                    self.isletim_sistemi.append(win11)
                    print("{} Yüklendi! Bilgisayarı Yeniden Açmayı Unutmayın...".format(win11))
                    self.kapat()
                elif secim == "3":
                    lin="Linux"
                    print("{} Sistemi Yükleniyor...\nLütfen Bekleyiniz...".format(lin))
                    time.sleep(3)
                    self.isletim_sistemi.append(lin)
                    print("{} Yüklendi! Bilgisayarı Yeniden Açmayı Unutmayın...".format(lin))
                    self.kapat()
                elif secim == "4":
                    un="Unix"
                    print("{} Sistemi Yükleniyor...\nLütfen Bekleyiniz...".format(un))
                    time.sleep(3)
                    self.isletim_sistemi.append(un)
                    print("{} Yüklendi! Bilgisayarı Yeniden Açmayı Unutmayın...".format(un))
                    self.kapat()
                else:
                    print("Geçersiz Seçim!")
            else:
                print("Birden Fazla İşletim Sistemi Kuramazsınız!\nLütfen Mevcut Sistemi Silin!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def isletim_sistemi_sil(self):
        if self.pc_durumu == "Açık":
            if self.isletim_sistemi == list():
                print("Silinecek Sistem Bulunamadı!")
            else:
                secim=input("{} Sistemini Silmek İstediğinize Emin Misiniz(Y/N): ".format(self.isletim_sistemi))
                if secim == "Y":
                    print("Sistem Siliniyor...\nLütfen Bekleyiniz...")
                    time.sleep(3)
                    self.isletim_sistemi.pop(0)
                    print("Sistem Silindi! Bilgisayarı Yeniden Açmayı Unutmayınız!")
                    self.kapat()
                else:
                    print("Sistem Silinmedi!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def uygulama_yükle(self):
        if self.pc_durumu == "Açık":
            print("""
            YÜKLENEBİLECEK UYGULAMALAR
            
            1-Steam
            2-Discord
            3-MS Teams
            4-MS Store
            5-Defender
            """)
            secim=input("Yüklemek İstediğiniz Uygulamanın Numarasını Giriniz: ")
            if secim == "1":
                print("Steam Yükleniyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.uygulamalar.append("Steam")
                print("Steam Yüklendi!")
            elif secim == "2":
                print("Discord Yükleniyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.uygulamalar.append("Discord")
                print("Discord Yüklendi!")
            elif secim == "3":
                print("MS Teams Yükleniyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.uygulamalar.append("MS Teams")
                print("MS Teams Yüklendi!")
            elif secim == "4":
                print("MS Store Yükleniyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.uygulamalar.append("MS Store")
                print("MS Store Yüklendi!")
            elif secim == "5":
                print("Defender Yükleniyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.uygulamalar.append("Defender")
                print("Defender Yüklendi!")
            else:
                print("Geçersiz Seçim!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def uygulama_sil(self):
        if self.pc_durumu == "Açık":
            print(self.uygulamalar)
            silinecek = int(input("Silmek İstediğiniz Uygulamanın Sırasını Giriniz: "))
            if silinecek > 0 and silinecek <= len(self.uygulamalar)+1:
                print("Uygulama Siliniyor...")
                time.sleep(1)
                self.uygulamalar.remove(self.uygulamalar[silinecek - 1])
                print("Uygulama Silindi")
            else:
                print("Silinecek Uygulama Bulunamadı!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def cihaz_bagla(self):
        if self.pc_durumu == "Açık":
            print("""
            BAĞLANABİLECEK CİHAZLAR

            1-Klavye
            2-Kulaklık
            3-Kart Okuyucu
            4-Oyun Kolu
            """)
            secim = input("Bağlamak İstediğiniz Cihazın Numarasını Giriniz: ")
            if secim == "1":
                print("Klavye Bağlanıyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.baglı_cihazlar.append("Klavye")
                print("Klavye Bağlandı!")
            elif secim == "2":
                print("Kulaklık Bağlanıyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.baglı_cihazlar.append("Kulaklık")
                print("Kulaklık Bağlandı!")
            elif secim == "3":
                print("Kart Okuyucu Bağlanıyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.baglı_cihazlar.append("Kart Okuyucu")
                print("Kart Okuyucu Bağlandı!")
            elif secim == "4":
                print("Oyun Kolu Bağlanıyor!\nLütfen Bekleyiniz...")
                time.sleep(2)
                self.baglı_cihazlar.append("Oyun Kolu")
                print("Oyun Kolu Bağlandı!")
            else:
                print("Geçersiz Seçim!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def cihaz_kaldır(self):
        if self.pc_durumu == "Açık":
            print(self.baglı_cihazlar)
            silinecek = int(input("Kaldırmak İstediğiniz Cihazın Sırasını Giriniz: "))
            if silinecek > 0 and silinecek <= len(self.baglı_cihazlar) + 1:
                print("Cihaz Kaldırılıyor...")
                time.sleep(1)
                self.baglı_cihazlar.remove(self.baglı_cihazlar[silinecek - 1])
                print("Cihaz Kaldırıldı")
            else:
                print("Silinecek Cihaz Bulunamadı!")
        else:
            print("Bilgisayar Kapalı!\nÖnce Bilgisayarı Açınız!\n")
    def __len__(self):
        return len(self.uygulamalar)
    def __str__(self):
        return """
        BİLGİSAYAR BİLGİLERİ
        
        Bilgisayar Durumu: {}
        İşletim Sistemi: {}
        Yüklü Uygulamalar: {}
        Bağlı Cihazlar: {}
        """.format(self.pc_durumu,self.isletim_sistemi,self.uygulamalar,self.baglı_cihazlar)

bilgisayar=Bilgisayar()

print("""
    BİLGİSAYAR UYGULAMASI

    1-Bilgisayarı Aç
    2-Bilgisayarı Kapat
    3-Hesap Makinesini Aç
    4-İşletim Sistemi Yükle
    5-İşletim Sistemini Sil
    6-Uygulama Yükle
    7-Uygulama Sil
    8-Cihaz Bağla
    9-Cihaz Kaldır
    10-Uygulama Sayısı
    11- Bilgisayar Durumu

    Çıkmak için q'ya basınız.
    """)

while True:


    islem = input("İşlem Seçiniz: ")

    if islem == "q":
        print("Program Sonlandırılıyor...")
        time.sleep(1)
        break
    elif islem == "1":
        bilgisayar.ac()
    elif islem == "2":
        bilgisayar.kapat()
    elif islem == "3":
        bilgisayar.hesap_makinesi()
    elif islem == "4":
        bilgisayar.isletim_sistemi_ekle()
    elif islem == "5":
        bilgisayar.isletim_sistemi_sil()
    elif islem == "6":
        bilgisayar.uygulama_yükle()
    elif islem == "7":
        bilgisayar.uygulama_sil()
    elif islem == "8":
        bilgisayar.cihaz_bagla()
    elif islem == "9":
        bilgisayar.cihaz_kaldır()
    elif islem == "10":
        print(len(bilgisayar.uygulamalar))
    elif islem == "11":
        print(bilgisayar)
    else:
        print("Geçersiz İşlem...")
