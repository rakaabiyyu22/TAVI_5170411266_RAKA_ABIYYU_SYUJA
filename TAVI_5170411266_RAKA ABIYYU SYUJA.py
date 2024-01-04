class PendidikanMinatDanBakat:
    def __init__(self, nama, nim):
        self._nama = nama  
        self._nim = nim
        self._minat = []
        self._bakat = []

    def tambah_minat(self, *minat):
        self._minat.extend(minat)

    def tambah_bakat(self, *bakat):
        self._bakat.extend(bakat)

    def tampilkan_minat(self):
        if self._minat:
            print(f"{self._nama} memiliki minat dalam:")
            for minat in self._minat:
                print(f"- {minat}")
        else:
            print("Belum ada minat yang teridentifikasi.")

    def tampilkan_bakat(self):
        if self._bakat:
            print(f"{self._nama} memiliki bakat dalam:")
            for bakat in self._bakat:
                print(f"- {bakat}")
        else:
            print("Belum ada bakat yang teridentifikasi.")

    def tampilkan_info(self):
        if self._nim < 5180411001:
            print(f"{self._nama} adalah mahasiswa prodi informatika tingkat akhir.")
        elif 5180411001 <= self._nim < 5230411001:
            print(f"{self._nama} adalah mahasiswa prodi informatika.")
        else:
            print(f"{self._nama} adalah mahasiswa baru informatika")

    def tampilkan_kombinasi(self, other):
        for minat in self._minat:
            for bakat in other._bakat:
                print(f"{self._nama} tertarik pada {minat} dan memiliki bakat dalam {bakat}.")


class PendidikanMinatProgrammer(PendidikanMinatDanBakat):
    def __init__(self, nama, nim):
        super().__init__(nama, nim)
    
    def tambah_minat(self, *minat):
        for m in minat:
            self._minat.append(m + " (Programming)")

    def tambah_bakat(self, *bakat):
        for b in bakat:
            self._bakat.append(b)

    def tampilkan_minat(self):
        if self._minat:
            print(f"{self._nama} memiliki minat dalam bidang pemrograman:")
            for minat in self._minat:
                print(f"- {minat}")
        else:
            print("Belum ada minat pemrograman yang teridentifikasi.")

    def tampilkan_bakat(self):
        if self._bakat:
            print(f"{self._nama} memiliki beragam bakat, namun bakat pemrograman adalah yang paling menonjol.")
            for bakat in self._bakat:
                print(f"- {bakat}")
        else:
            print("Belum ada bakat yang teridentifikasi.")

class PendidikanMinatDesain(PendidikanMinatDanBakat):
    def tambah_minat(self, *minat):
        super().tambah_minat(*[m + " (Desain)" for m in minat])

    def tampilkan_minat(self):
        if self._minat:
            print(f"{self._nama} memiliki minat dalam bidang desain:")
            for minat in self._minat:
                print(f"- {minat}")
        else:
            print("Belum ada minat desain yang teridentifikasi.")

    def tampilkan_bakat(self):
        print(f"{self._nama} memiliki bakat-bakat yang mendukung di bidang desain.")


class PendidikanMinatKeuangan(PendidikanMinatDanBakat):
    def tambah_minat(self, *minat):
        super().tambah_minat(*[m + " (Keuangan)" for m in minat])

    def tampilkan_minat(self):
        if self._minat:
            print(f"{self._nama} memiliki minat dalam bidang keuangan:")
            for minat in self._minat:
                print(f"- {minat}")
        else:
            print("Belum ada minat keuangan yang teridentifikasi.")

    def tampilkan_bakat(self):
        print(f"{self._nama} memiliki bakat-bakat yang mendukung di bidang keuangan.")


def tampilkan_pilihan():
    print("Pilihan Minat:")
    print("1. Pemecahan Masalah")
    print("2. Analisis Data")
    print("3. Desain")
    print("4. Networking")
    print("5. Kreativitas")
    print("6. Kolaborasi")

    print("\nPilihan Bakat:")
    print("1. Pemecahan Masalah")
    print("2. Kreativitas")
    print("3. Kolaborasi")
    print("4. Manajemen Waktu")
    print("5. Kepemimpinan")


while True:
    print("\n=== PROGRAM PENDIDIKAN MINAT DAN BAKAT ===")
    nama = input("Masukkan Nama: ")
    nim = int(input("Masukkan Nim: "))

    print("=== PILIHAN BIDANG ===")
    print("1. Pemrograman")
    print("2. Desain")
    print("3. Keuangan")
    pilihan_bidang = int(input("Pilih bidang (masukkan nomor): "))
    
    if pilihan_bidang == 1:
        individu1 = PendidikanMinatProgrammer(nama, nim)
    elif pilihan_bidang == 2:
        individu1 = PendidikanMinatDesain(nama, nim)
    elif pilihan_bidang == 3:
        individu1 = PendidikanMinatKeuangan(nama, nim)
    else:
        print("Pilihan tidak valid.")
        continue
    
    tampilkan_pilihan()
    pilihan_minat = [int(x) for x in input("Pilih minat (pisahkan dengan koma jika lebih dari satu): ").split(',')]
    pilihan_bakat = [int(x) for x in input("Pilih bakat (pisahkan dengan koma jika lebih dari satu): ").split(',')]
    
    daftar_minat = {1: "Pemecahan Masalah", 2: "Analisis Data", 3: "Desain", 4: "Networking", 5: "Kreativitas", 6: "Kolaborasi"}
    daftar_bakat = {1: "Pemecahan Masalah", 2: "Kreativitas", 3: "Kolaborasi", 4: "Manajemen Waktu", 5: "Kepemimpinan"}
    
    minat_terpilih = [daftar_minat[pilihan] for pilihan in pilihan_minat]
    bakat_terpilih = [daftar_bakat[pilihan] for pilihan in pilihan_bakat]
    
    individu1.tambah_minat(*minat_terpilih)
    individu1.tambah_bakat(*bakat_terpilih)
    
    individu1.tampilkan_minat()
    individu1.tampilkan_bakat()
    individu1.tampilkan_info()
    
    lanjut = input("\nApakah ingin memasukkan data lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break
