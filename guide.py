rehber_dizi=[]
#################################-Anasayfa--##########################################
def anasayfa():
    print(""" 
              --------------------
              1:Kişi Ekle
              2:Kişi Sil
              3:Kişi Düzenle
              4:Kişileri Gör
              5:Uygulamayı kapat
              --------------------
          """)
    sec = int(input("Yapacağınız işlemi seçiniz:"))
    if sec == 1:
        Rehber.no_kaydet()
    if sec ==2:
        Rehber.no_sil()
    if sec == 3:
        Rehber.kisi_duzenle()
    if sec ==4:
        Rehber.rehberi_gor()
    if sec ==5:
        quit()
###########################-Kaydet,Sil,Düzenle,Göster-############################
class Rehber:
    def no_kaydet():
        ad = input("Adını giriniz: ")
        soyad= input("Soyadını giriniz: ")
        try :
            no = int(input("Numarayı giriniz: "))
        except ValueError:
            print("Bilinmeyen bir hata oluştur,lütfen tekrar deneyiniz.")
            return
        print("Başarıyla kaydedildi !")
        print(f"""
              Adı : {ad}, 
              Soyadı : {soyad},
              Numara :{no} """)
        rehber_dizi.append({"ad": ad, "soyad": soyad, "no": no})

    def no_sil():
        kisi_id_remove=None
        for kisi_id, item in enumerate(rehber_dizi):
            kisi_id_remove = kisi_id
            print(f"Id {kisi_id}: {item}")
        try:
            sil_no=int(input("Silinecek kişinin ID'sini yazınız: "))
        except ValueError:
            print("Bilinmeyen bir hata oluştu,tekrar id yaz.")
            return

        if kisi_id_remove is not None:
            removed_kisi = rehber_dizi.pop(kisi_id_remove)
            print("Kişi silindi.")
            Rehber.rehberi_gor()

    def kisi_duzenle():
        Rehber.rehberi_gor()
        if not rehber_dizi:
            print("Rehberde kayıtlı kişi bulunmuyor.")
            return

        try:
            id = int(input("Kişinin IDsini giriniz: "))
        except ValueError:
            print("Bilinmeyen bir hata oluştu, tekrar ID giriniz.")
            return

        for kisi_id, kisi in enumerate(rehber_dizi):
            if kisi_id == id:
                yeni_ad = input("Yeni ad giriniz: ")
                yeni_soyad = input("Yeni soyad giriniz: ")
                try:
                    yeni_no = int(input("Yeni numara giriniz: "))
                except ValueError:
                    print("Bilinmeyen bir hata oluştu, tekrar numara giriniz.")
                    return

                kisi["ad"] = yeni_ad
                kisi["soyad"] = yeni_soyad
                kisi["no"] = yeni_no
                print("Kişi bilgileri güncellendi.")
                return
        print("Belirtilen ID'ye sahip kişi bulunamadı.")
    def rehberi_gor():
        for kisi_id, item in enumerate(rehber_dizi):
            print(f"Id {kisi_id}: {item}")
###############################################################################
while True:
    if __name__ == '__main__':
        anasayfa()
