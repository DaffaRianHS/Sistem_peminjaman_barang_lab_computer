barang = ["laptop", "tablet", "handphone"]
dipinjam = []
tidak_tersedia = []

while True:
    selection = input("Mau meminjam barang atau mengubah barang? (1:meminjam, 2:mengubah, 3: selesai):")

    if selection == "2":
        modify = input("Mau mengubah status barang atau mengedit barang yang ada? (1:mengubah status, 2:edit barang)")
        if modify == "2":
            while True:
                print(barang)
                edit = input("Jika ingin menambah barang, silakan diketik, jika tidak, ketik 'hapus' untuk menghapus barang, jika udah selesai, ketik 'exit':")
                if edit == "hapus":
                    modifydel = input("Masukkan barang yang mau dihapus:")
                    if modifydel in barang:
                        barang.remove(modifydel)
                        print(f"Barang {modifydel} telah dihapus")
                    else:
                        print("Barang tidak ditemukan")
                elif edit == "exit":
                    break
                else:
                    barang.append(edit)
                    print(f"Barang {edit} telah ditambah")
                    confirm = input("Apakah ingin mengambah barang lagi? (y/n):")
                    if confirm == "y":
                        continue
                    else:
                        break
                    
        else:
            while True:
                print(f"Barang yang tersedia: {barang}")
                print(f"Barang yang tidak tersedia: {tidak_tersedia}")
                select = input("Masukkan barang yang ingin dirubah statusnya (ketik 'exit' untuk keluar):")
                if select in barang:
                    confirm = input("Apakah anda mau bikin barang ini tidak tersedia? (y/n)")
                    if confirm == "y":
                         barang.remove(select)
                         tidak_tersedia.append(select)
                         print(f"Barang {select} telah dibikin tidak tersedia")
                    else:
                        continue
                elif select in tidak_tersedia:
                        confirm = input("Apakah anda mau bikin barang ini tersedia? (y/n)")
                        if confirm == "y":
                            tidak_tersedia.remove(select)
                            barang.append(select)
                            print(f"Barang {select} telah dibikin tersedia")
                        else:
                            continue
                elif select == "exit":
                    break
                else:
                    print("Barang tidak ditemukan")

    elif selection == "1":
        while True:
            print(f"Barang yang tersedia: {barang}")
            select = input("Pilih barang yang ingin dipinjam (ketik 'exit' untuk keluar):")

            if select in barang:
                barang.remove(select)
                dipinjam.append(select)
                print(f"Barang {select} telah dipinjam")
                confirm = input("Apakah ingin meminjam barang lagi? (y/n):")
                if confirm == "y":
                    continue
                else:
                    break
            elif select == "exit":
                break
            else:
                print("Barang tidak ditemukan, dipinjam, atau tidak tersedia")
    else:
        break

print("===========HASIL BARANG YANG DIPINJAM===========")
print(f"Barang tersedia: {barang}")
print(f"Barang tidak tersedia: {tidak_tersedia}")
print(f"Barang yang dipinjam: {dipinjam}")