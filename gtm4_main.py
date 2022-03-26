# array, kumpulan data disimpan
pilA =["ambatukam","pico","wuhan","pp"]
pilB = ["acumalaka","japanis gobolin","amogus"]
pilC = ["osas","kodok","cicak"]

# fungsi untuk menambahkan data peserta survey
def imenu1(md, inama):
    if md == 1:
        pilA.insert(len(pilA), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 2:
        pilB.insert(len(pilB), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 3:
        pilC.insert(len(pilC), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam survey")
    else:
        return print(" <<Pilihan ini tidak tersedia")
    
 # fungsi untuk menampilkan data peserta yang telah malakukan survey  
def imenu2(n):
    print(" >Memilih pro Rusia ("+str(len(pilA))+" pendukung)")
    for n in range (len(pilA)):
        print("  "+str(n+1), pilA[n])
    print(" >Memilih pro Ukraina ("+str(len(pilB))+" pendukung)")
    for n in range (len(pilB)):
        print(f"  "+str(n+1), pilB[n])
    print(" >Netral ("+str(len(pilC))+" pendukung)")
    for n in range (len(pilC)):
        print("  "+str(n+1), pilC[n])
 
# fungsi untuk menampilkan persentase dari data seurvey
def imenu3():
    t = len(pilA) + len(pilB) + len(pilC)
    pa = 100 * len(pilA) / t 
    pb = 100 * len(pilB) / t 
    pc = 100 * len(pilC) / t 
    ipa = int(pa)
    ipb = int(pb)
    ipc = int(pc)
    return print("   Terdata perserta survey adalah "+str(t)+" orang\n   1. Pendukung Rusia "+str(ipa)+"%\n   2. pendukung Ukraina "+str(ipb)+"%\n   3. Netral "+str(ipc)+"%")


# progam utama
from gtm4_c1 import *
lp = 0
while True:
    print("\n\n=========SURVEY=========")
    mkr = mthd("DIDID BAYU FARIZQI","LUTHFI ANIS SYAFAR","ADDELLIA DEVIANTI","RIZAL AGATHA ERDIN AGESYAH")
    print("Survey by: Shift 1, Kelompok 3: \n<> "+mkr.n1+"\n<> "+mkr.n2+"\n<> "+mkr.n3+"\n<> "+mkr.n4)    
    print("-<({[MENU]})>-:")
    print("A. menambah data survey\nB. menampilkan data\nC. melihat persentase")
    imenu = input(">pilih huruf angka dari pilihan menu: ")
    print("")

    if imenu == 'a' or imenu == 'A':
        print("---Menambah Data Survey---")
        inama = input(" >masukkan nama anda: ")
        print(" >pilihan untuk didukung:")
        print("  1. Pilih pro Rusia\n  2. Pilih pro Ukaraina\n  3. Netral")
        md = int(input(" <masukkan nomor angka: "))
        imenu1(md, inama) 
    elif imenu == 'b' or imenu == 'B':
        print("---List Data Survey---") 
        imenu2(0)
    elif imenu == 'c' or imenu == 'C':
        print("---Persentase Data Survey---")
        imenu3()
    else:
        print(">>pilihan tidak ada dalam menu")
    
    if imenu == 'a' or imenu == 'A' or imenu == 'b' or imenu == 'B' or imenu == 'c' or imenu == 'C':
        lp+=1
    
    print("")
    mkr.selesai(lp)    
