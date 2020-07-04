class mhsTIF():
    def __init__(self, nama, asal, saku):
        self.nama = nama
        self.asal = asal
        self.saku = saku
c0 = mhsTIF('a','sukoharjo',240000)
c1 = mhsTIF('b','klaten', 260000)
c2 = mhsTIF('c','salatiga',280000)
c3 = mhsTIF('d','klaten',200000)
c4 = mhsTIF('e','surakarta',200000)
c5 = mhsTIF('f','salatiga',290000)
c6 = mhsTIF('g','sukoharjo',230000)

daftar = [c0,c1,c2,c3,c4,c5,c6]

print('\nNOMOR 1')
def cari(n):
    baru = []
    for i in range(len(n)):
        if(n[i].asal.lower() == 'klaten'):
            baru.append(i)
    return baru
print(cari(daftar))

print('\nNOMOR 2')
def sakuKcl(n):
    baru = n[0].saku
    for i in range(len(n)):
        if(n[i].saku<baru):
            baru = n[i].saku
    return baru
print(sakuKcl(daftar))

print('\nNOMOR 3')
def sakuKcl2(n):
    baru = n[0].saku
    list = []
    for i in range(len(n)):
        if(n[i].saku==baru):
            list.append(n[i].nama)
        elif(n[i].saku<baru):
            baru = n[i].saku
            list = []
            list.append(n[i].nama)
    return list
print(sakuKcl2(daftar))

print('\nNOMOR 4')
def sakuKrg(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].saku < batas):
            list.append(n[i].nama)
    return list
print(sakuKrg(daftar))

print('\nNOMOR 5')
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        return self.head
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            
llist = LinkedList() 
llist.pushAw(21)
llist.pushAw(22)
llist.pushAw(12)
llist.pushAw(14)
llist.pushAw(2)
llist.pushAw(19)
print(llist.search(21))
print(llist.search(29))

print('\nNOMOR 6')
def binSe(list, target):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            return "target di index "+str(mid)
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid +1
    return "target tidak ditemukan di index berapapun"
list = [2,4,6,9,12,27,39,46,59,77]
target = 12
print(binSe(list,target))
list = [2,4,6,9,12,27,39,46,59,77]
target = 133
print(binSe(list,target))

print('\nNOMOR 7')
def binSe(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False
kumpulan = [2
,3,4,5,8,8,9,12]
target = 8
print(binSe(kumpulan,target))


