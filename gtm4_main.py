# array, kumpulan data disimpan
pilA =["ambatukam","pico","wuhan","pp"]
pilB = ["acumalaka","japanis gobolin","amogus"]
pilC = ["osas","kodok","cicak"]














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