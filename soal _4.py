class Buah:
    def _init_(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def atur_nama(self, nama):
        self.nama = nama

    def atur_warna(self, warna):
        self.warna = warna

    def atur_rasa(self, rasa):
        self.rasa = rasa

    def informasi(self):
       
        print(f"Nama Buah: {self.nama}")
        print(f"Warna Buah: {self.warna}")
        print(f"Rasa Buah: {self.rasa}")

class KelolaBuah(Buah):
    def _init_(self, nama, warna, rasa, vitamin):
        super()._init_(nama, warna, rasa)
        self.vitamin = vitamin

    def atur_vitamin(self, vitamin):
        self.vitamin = vitamin

    def informasi(self):
        """Menampilkan informasi buah beserta vitaminnya"""
        super().informasi()
        print(f"Vitamin Buah: {self.vitamin}")

if _name_ == "_main_":
 
    buah = KelolaBuah("Apel", "Merah", "Manis", "Vitamin C")

    buah.informasi()
    
    buah.atur_nama("Pisang")
    buah.atur_warna("Kuning")
    buah.atur_rasa("Manis")
    buah.atur_vitamin("Vitamin B6")

    print("\nInformasi setelah perubahan:")
    buah.informasi()