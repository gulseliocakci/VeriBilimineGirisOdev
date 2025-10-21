# Üst sınıf: İnsan
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir insanım.")

# Alt sınıf: Hoca
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir hocayım. Ders vermeyi çok severim.")

    def ders_ver(self):
        print(f"{self.ad} (Sicil No: {self.sicil_no}) şu anda ders veriyor.")

# Alt sınıf: Sekreter
class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman

    def konus(self):
        print(f"{self.ad}: Merhaba, ben {self.departman} departmanında sekreter olarak çalışıyorum.")

    def randevu_ayarla(self, kisi):
        print(f"{self.ad}: {kisi} için randevu ayarladım.")

# Alt sınıf: Öğrenci
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no, bolum):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no
        self.bolum = bolum

    def konus(self):
        print(f"{self.ad}: Merhaba, ben {self.bolum} bölümünde öğrenciyim.")

    def ders_calıs(self):
        print(f"{self.ad}: Şu anda ders çalışıyorum.")

# --- Örnek Kullanım ---

# İnsan nesnesi
i1 = Insan("Ali", 30)
i1.konus()

# Hoca nesnesi
h1 = Hoca("Ayşe Hoca", 45, "H1234")
h1.konus()
h1.ders_ver()

# Sekreter nesnesi
s1 = Sekreter("Fatma", 35, "Öğrenci İşleri")
s1.konus()
s1.randevu_ayarla("Ahmet")

# Öğrenci nesnesi
o1 = Ogrenci("Mehmet", 20, "20231234", "Bilgisayar Mühendisliği")
o1.konus()
o1.ders_calıs()