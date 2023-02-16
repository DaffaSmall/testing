import random


uang = 0
point = 0

Barang =  [{"nama_barang": "Tisu", "harga": 20, "ada":False},
           {"nama_barang": "Buku", "harga": 20, "ada":False},
           {"nama_barang": "Sayuran", "harga": 15, "ada":False}]


    #for nomor, benda in enumerate(Barang):
    #    print(str(nomor + 1)+ ":", benda["nama_barang"]+":", benda["harga"])
#
    #pilihan = int(input("input pilihan yang mau beli: "))
    #if not Barang[pilihan]["bisa_diricycle"]:
    #    point -= 1
    #    print("point dikurang 1")
    #else:
    #    point += 1
    #    print("point ditambah 1")
while True:
    print("""uang: {0}
point: {1}""".format(uang, point))
    inputs = input("Nama barang yang mau dijual: ")
    for y, x in enumerate(Barang):
        if x["nama_barang"] == inputs:
            Barang[y]["ada"] = True
            point += x["harga"]