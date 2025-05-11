print("<              nama toko             >")
print("<----------------MENU---------------->")
print("<----1-------chikenjhokey------------>")
print("<----2-------burgersigma------------->")
print("<----3-------pizzaauuuuu------------->")
print("<----4-------mieayamlejat------------>")
print("<----5-------baksow------------------>")
print("ISI SESUAI DENGAN MENU YG ANDA PILIH!!")

pilihan = input("mw yg mana ? ").lower()

if pilihan == "chikenjhokey":
    harga = 20000
    try:
        jumlah = int(input("Mau berapa ? "))
        total = harga * jumlah
        print(f"harga: Rp.{harga}")
        print(f"total harga: Rp.{total}")
    except ValueError:
        print("input harus angka bukan selain itu")
elif pilihan == "burgersigma":
    harga =25000
    try:
        jumlah = int(input("mw brp? "))
        total = harga * jumlah
        print(f"harga: Rp.{harga}")
        print(f"total harga: Rp.{total}")
    except ValueError:
        print("input harus angka bukan selain itu")
elif pilihan == "pizzaauuuuu":
    harga = 35000
    try:
        jumlah = int(input("mw brp? "))
        total = harga * jumlah
        print(f"harga: Rp.{harga}")
        print(f"total harga: Rp.{total}")
    except ValueError:
        print("input harus angka bukan selain itu")
elif pilihan == "mieayamlejat":
    harga = 7000
    try:
        jumlah = int(input("mw brp? "))
        total = harga * jumlah
        print(f"harga: Rp.{harga}")
        print(f"total: Rp.{total}")
    except ValueError:
        print("input harus angka bukan selain itu")
elif pilihan == "baksow":
    harga = 7000
    try:
        jumlah = int(input("mw brp? "))
        total = harga * jumlah
        print(f"harga: Rp.{harga}")
        print(f"total: Rp.{total}")
    except ValueError:
        print("input harus angka bukan selain itu")
elif pilihan == "rahasia":
    harga = 0
    try:
        print("nice code")
        print("paket: semua")
        print(f"harga: {harga}")
    except ValueError:
        print("salah")
else:
    print("Menu tidak ditemukan / salah ketik.")
