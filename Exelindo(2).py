# Nama : Exelindo Yeremia
# Nim : 190402145
# Ujian Akhir Semester Pemrograman Komputer TE-D

# section 1 : Membuat dengan hasil print ('Str', 'float' , 'Int')
M = "Mangga"
L = 1.0
c = 2
print(M,L,c) # Hasil (Mangga 1.0 2)
print(M) # Hasil(Mangga)
print(L) # Hasil(1.0)
print(c) # Hasil (2)

# section 2 : Menentukkan tipe dari hasil print
z = 3.4, 3.5
d = 4 , 20
f = "Billaaa", "elaa"
g = 5.0
l = 6
p = "papa"
print(type(z)) # <class 'tuple'>
print(type(d)) # <class 'tuple'>
print(type(f)) # <class 'tuple'>
print(type(g)) # <class 'float'>
print(type(l)) # <class 'int'>
print(type(p)) # <class 'str'>

# Section 3 : Python Number
# koordinat di titik P (2, 3)
x,y = 2, 3
y,x = 3, 2
print(x,y) # 2 3
print(y,x) # 3 2

# Section 4 : memotong huruf pada kalimat berdasarkan peletakan huruf
Mama = "Belikkan dulu mama beras 1 kg"
print(Mama) # Belikkan dulu mama beras 1 kg
print(Mama[::-2]) # g  ae mmuu aklB
print(Mama[:2]) # Be
print(Mama[2:]) #  likkan dulu mama beras 1 kg
print(Mama.upper()) # BELIKKAN DULU MAMA BERAS 1 KG
print(Mama.lower()) # belikkan dulu mama beras 1 kg
print(Mama.replace("B","D")) # Delikkan dulu mama beras 1 kg

# Section 5 : Python List
hei = "Eddo%5 lagi%5 makan"
didit =hei.split('%5') #  %5 menjadi koma
print(didit) # hasilnya menjadi['Eddo', ' lagi', ' makan']

# Section 6 : Kombianasi Python list 
Buah = ['durian', 'anggur', 'pisang', 'jeruk']
print(Buah) # ['durian', 'anggur', 'pisang', 'jeruk']
print(type (Buah)) # hasilnya masih list
jus =''.join(Buah)
print(jus) # hasilnya duriananggurpisangjeruk
print(type (jus))# Setelah dimasukkan ke variabel jus hasilnya menjadi string

# section 7 : Menghitung jumlah angka dalam list
Angka = [1,4,3,1,4,3,5,6,7,6,7,8,9,9,9,9]
print(Angka.count(1)) # Jumlah Angka 1 sebanyak 2
print(Angka.count(4)) # Jumlah Angka 4 sebanyak 2
print(Angka.count(3)) # Jumlah Angka 3 sebanyak 2
print(Angka.count(5)) # Jumlah Angka 5 sebanyak 1
print(Angka.count(6)) # Jumlah Angka 6 sebanyak 2
print(Angka.count(7)) # Jumlah Angka 7 sebanyak 2
print(Angka.count(8)) # jumlah Angka 8 sebanyak 1
print(Angka.count(9)) # Jumlah Angka 9 sebanyak 4

# Section 8 : Memperbesar,memperkecil kalimat
name = "GLOMA SIBURIAN"
name2 = "golma siburian"
print(name.upper()) # GLOMA SIBURIAN
print(name.lower()) # gloma siburian
print(name.capitalize()) # Gloma siburian
print(name2.upper()) # GOLMA SIBURIAN
print(name2.lower()) # golma siburian
print(name2.capitalize()) # Golma siburian

# Section 9 : 
kegiatan = [ "makan", "minum", "belajar", "tidur", "nonton"]
kegiatan_baru = map(str.upper, kegiatan) # Semua kata akan huruf besar
kegiatan_baru2 = map(str.capitalize, kegiatan) # Semua kata huruf awalannya adalah huruf besar
kegiatan_baru3 = map(str.lower, kegiatan) # Semua huruf akan huruf kecil
print(list(kegiatan_baru)) # ['MAKAN', 'MINUM', 'BELAJAR', 'TIDUR', 'NONTON']
print(list(kegiatan_baru2)) # ['Makan', 'Minum', 'Belajar', 'Tidur', 'Nonton']
print(list(kegiatan_baru3)) # ['makan', 'minum', 'belajar', 'tidur', 'nonton']

kegiatan = ( "makan", "minum", "belajar", "tidur", "nonton")
kegiatan_baru = map(str.upper, kegiatan) # Semua kata akan huruf besar
kegiatan_baru2 = map(str.capitalize, kegiatan) # Semua kata huruf awalannya adalah huruf besar
kegiatan_baru3 = map(str.lower, kegiatan) # Semua huruf akan huruf kecil
print(tuple(kegiatan_baru)) # ('MAKAN', 'MINUM', 'BELAJAR', 'TIDUR', 'NONTON')
print(tuple(kegiatan_baru2))  #('Makan', 'Minum', 'Belajar', 'Tidur', 'Nonton')
print(tuple(kegiatan_baru3)) #('makan', 'minum', 'belajar', 'tidur', 'nonton')



# Section 10 : Menyebutkan angka dalam range yang telah ditentukan
rangka = [ z for z in range (10,19)]; # Angka dalam range yaitu 10-19
print(rangka) # [10, 11, 12, 13, 14, 15, 16, 17, 18] 

# Section 11 : Python dictionary
Kamus = {
  "Nama": "Lina",
  "Tahun": 2001,
  "Zodiak" : "Gemini"
}
print(Kamus) # Sesuai penyusunan pada dictionary
  
 # Section 12 : Memanggil fungsi ( Python Function)
def martabak (): # mendefinisikan suatu fungsi pertama
    print("Saya pengen membeli martabak bangka")

def BanyaknyaMartabak(): # masih dalam proses mendefinsikan suatu fungsi kedua
    print("Bang saya pesan martabaknya 3")

BanyaknyaMartabak() # memanggil fungsi yang kedua
# Kesimpulan : Ketika mendefinisikan fungsi 1 dan 2 jika kita memanggil fungsi
# setelah pada fungsi kedua maka yang akan keluar adalah fungsi kedua saja

# Section 13 : Memanggil fungsi (Python Function) Part II
def ela (): # Mendefinisikan suatu fungsi pertama
    print("ela akan pergi ke rumah temannya" )

def Sianghari ():# Mendefinisikan suatu fungsi kedua
    ela() # Memangggil fungsi pada pertama
    print("Pada siang hari, ela akan menuju ke rumah temannya")

Sianghari() # Memanggik fungsi pada kedua
# Kesimpulan : Fungsi 1 &  2 akan  terpanggil jika kita memanggil fungsi nya 
# secara masing - masing

# Section 14 : Python object opsional
class Saudara :
      pass

Saudara1 = Saudara() # opsi 1
Saudara2 = Saudara() # opsi 2
Saudara3 = Saudara(); # opsi 3

Saudara1.nama = "George Michael"
Saudara1.umur = 22

Saudara2.nama = "Rachel Gracia"
Saudara2.umur = 17

Saudara3.nama = "KaylaSubaini" 
Saudara3.umur = 9

print(Saudara1.__dict__) # {'nama': 'George Michael', 'umur': 22}
print(Saudara2.__dict__) # {'nama': 'George Michael', 'umur': 22}
print(Saudara3.__dict__) # {'nama': 'KaylaSubaini', 'umur': 9}

# Section 15 : 
