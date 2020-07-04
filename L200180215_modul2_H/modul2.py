#2
class Pesan(object):
    """
        Sebuah class bernama pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, x):
        if x in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        konsonan = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
        a = 0
        for i in self.teks:
            if i in konsonan:
                a += len(i)
            else:
                a += 0
        return a
    def hitungVokal(self):
        vokal = 'euioaEUIOA'
        a = 0
        for i in self.teks:
            if i in vokal:
                a += len(i)
            else:
                a += 0
        return a

    #3
class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self,s):
        print("Saya beru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

p1 = Manusia('Fatimah')
p1.ucapkanSalam()

class SiswaSMA():
    def __init__(self,nama,kelas):
        self.namaSiswa = nama
        self.kelas = kelas
    def ambilNama(self):
        return self.namaSiswa
    def ambilKelas(self):
        return self.kelas
    def gantiNama(self,nama):
        self.nama = nama
    def gantiKelas(self,kelas):
        self.kelas = kelas

#4
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kota):
        self.kotaTinggal = kota
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,us):
        self.uangSaku = self.uangSaku + us

    listKuliah = []
    def ambilKuliah(self,matkul):
        self.listKuliah.append(matkul)
    def hapusKuliah(self,matkul):
        self.listKuliah.remove(matkul)

print('Masukkan nama:')
nama = input()
print('Masukkan nim:')
nim = input()
print('Masukkan kota:')
kota = input()
print('Masukkan uang saku:')
us = input()
us = int(us)
m1 = Mahasiswa(nama,nim,kota,us)


#5
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

#SOAL NO7
#NIM berasal dari class Mahasiswa
#ambilNIM berasal dari class Mahasiswa
#ambilNama berasal dari class Mahasiswa
#ambilUangSaku berasal dari class Mahasiswa
#katakanPy berasal dari class MhsTIF
#keadaan berasal dari class Manusia
#kotaTinggal berasal dari class Mahasiswa
#makan berasal dari class Manusia
#mengalikanDenganDua berasal dari class Manusia
#nama berasal dari class Mahasiswa dan Manusia
#listKuliah berasal dari class Mahasiswa
#ambilKuliah berasal dari class Mahasiswa
#hapusKuliah berasal dari class Mahasiswa
#tambahUangSaku berasal dari class Mahasiswa
#uangSaku berasal dari class Mahasiswa
#ambilKotaTinggal dari class Mahasiswa
#olahraga berasal dari class Manusia
#perbaruiKotaTinggal berasal dari class Mahasiswa
#ucapkanSalam berasal dari class Manusia
