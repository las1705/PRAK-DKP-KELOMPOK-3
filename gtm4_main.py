# array, kumpulan data disimpan
pilA =["ambatukam","pico","wuhan","pp"]
pilB = ["acumalaka","japanis gobolin","amogus"]
pilC = ["osas","kodok","cicak"]

def imenu1(md, inama):
    if md == 1:
        pilA.insert(len(pilA), inama)
        print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 2:
        pilB.insert(len(pilB), inama)
        print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 3:
        pilC.insert(len(pilC), inama)
        print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam survey")
    else:
        return print(" <<Pilihan ini tidak tersedia")
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
while True:
    print("\n\n=========Survey=========")
    print(">menu:")
    print("A. menambah data survey\nB. menampilkan data\nC. melihat persentase")
    imenu = input(">pilih huruf angka dari pilihan menu: ")
    print("")

    if imenu == 'a' or imenu == 'A':
        print("--Menambah Data Survey--")
    elif imenu == 'b' or imenu == 'B':
        print("--List Data Survey--")       
    elif imenu == 'c' or imenu == 'C':
        print("--Persentase Data Survey--")
    else:
        print("--pilihan tidak ada dalam menu--")
