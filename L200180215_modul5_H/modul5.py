class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')

Daftar = [MhsTIF ('Ika',110,'Sukoharjo', 240000),
MhsTIF('Budi',215,'Sragen', 230000),
MhsTIF('Ahmad',222,'Surakarta', 250000),
MhsTIF('Chandra',218,'Surakarta', 230000),
MhsTIF('Eka',214,'Boyolali', 240000),
MhsTIF('Fandi',321,'Salatiga', 250000),
MhsTIF('Deni',132,'Klaten', 245000),
MhsTIF('Galuh',522,'Wonogiri', 245000),
MhsTIF('Janto',223,'Klaten', 245000),
MhsTIF('Hasan',264,'Karanganyar', 270000),
MhsTIF('Khalid',129,'Purwodadi', 265000)]

#1
def ceknim (d):
    for i in d :
        print (i.NIM)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutnim(d):
    n = len(d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k].NIM > d[k+1].NIM :
                swap(d,k,k+1)
##cara menampilkan
##urutnim(Daftar)
##ceknim(Daftar)
#2
a = [2,6,7,9,4]
b = [5,8,10,3,1]
c = a + b

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urut(d):
    n = len (d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k] > d[k+1] :
                swap(d,k,k+1)

urut(c)
print(c)

#3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw = detak(); selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw = detak(); insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));

