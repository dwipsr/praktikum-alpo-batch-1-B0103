# Profil Karakter 
nama_hero = "Rexus"
level = 10
hp = 150.75
is_alive = True
inventory = ["Pedang", "Busur Mahabarata", "Belati"]
atribut = {"kekuatan": 80, "kelincahan": 65}

print("   INFORMASI KARAKTER AWAL   ")
print("Nama Hero   :", nama_hero)
print("Level       :", level)
print("HP          :", hp)
print("Status Hidup:", is_alive)
print("Inventory   :", inventory)
print("Atribut     :", atribut)

print("\n   TIPE DATA DARI MASING-MASING VARIABEL   ")
print("Tipe nama_hero  :", type(nama_hero))
print("Tipe level      :", type(level))
print("Tipe hp         :", type(hp))
print("Tipe is_alive   :", type(is_alive))
print("Tipe inventory  :", type(inventory))
print("Tipe atribut    :", type(atribut))

inventory.append("Ramuan HP")
level = float(level) + 0.5

print("\n   INFORMASI KARAKTER TERBARU   ")
print("Level Terbaru (Float) :", level)
print("Inventory Terbaru     :", inventory)