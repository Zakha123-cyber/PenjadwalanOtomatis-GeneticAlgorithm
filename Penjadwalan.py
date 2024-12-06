import random

# Inisialisasi parameter genetika
POP_SIZE = 50
MAX_GEN = 100
MUTATION_RATE = 0.1

# Representasi masalah dengan kode unik
mata_kuliah = [
    {"kode": "MK001", "nama": "Matematika"},
    {"kode": "MK002", "nama": "Fisika"},
    {"kode": "MK003", "nama": "Kimia"},
    {"kode": "MK004", "nama": "Biologi"},
    {"kode": "MK005", "nama": "Algo"}
]

waktu = [
    {"kode": "W001", "hari": "Senin", "jam": "08:00"},
    {"kode": "W002", "hari": "Senin", "jam": "10:00"},
    {"kode": "W003", "hari": "Selasa", "jam": "08:00"},
    {"kode": "W004", "hari": "Selasa", "jam": "10:00"},
    {"kode": "W005", "hari": "Senin", "jam": "14:00"}
]

ruangan = [
    {"kode": "R101", "nama": "Ruang 101"},
    {"kode": "R102", "nama": "Ruang 102"}
]

dosen = [
    {"kode": "D001", "nama": "Dosen A"},
    {"kode": "D002", "nama": "Dosen B"}
]

# Inisialisasi populasi
def inisialisasi_populasi():
    return [
        [
            random.choice(waktu),
            random.choice(ruangan),
            random.choice(dosen)
        ]
        for _ in mata_kuliah
    ]

# Fungsi fitness
def evaluasi_fitness(jadwal):    
    konflik = 0
    kombinasi_terpakai = set()
    for j in jadwal:
        kombinasi = (j[0]["kode"], j[1]["kode"])  # Kombinasi waktu dan ruangan
        if kombinasi in kombinasi_terpakai:
            konflik += 1
        kombinasi_terpakai.add(kombinasi)
    return -konflik

# Seleksi
def seleksi(populasi):
    populasi.sort(key=lambda x: evaluasi_fitness(x), reverse=True)
    return populasi[:2]

# Crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Mutasi
def mutasi(jadwal):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(jadwal) - 1)
        jadwal[index] = [
            random.choice(waktu),
            random.choice(ruangan),
            random.choice(dosen)
        ]
    return jadwal

# Algoritma Genetika
def main_genetic_algorithm():
    populasi = [inisialisasi_populasi() for _ in range(POP_SIZE)]

    for gen in range(MAX_GEN):
        populasi = [
            mutasi(child)
            for parent1, parent2 in zip(*[iter(seleksi(populasi))]*2)
            for child in crossover(parent1, parent2)
        ]
        if evaluasi_fitness(populasi[0]) == 0:
            break

    # Output solusi terbaik
    jadwal_terbaik = populasi[0]
    print("\nJadwal Terbaik:")
    for mk, jadwal in zip(mata_kuliah, jadwal_terbaik):
        print(
            f"{mk['nama']}: {jadwal[0]['hari']} {jadwal[0]['jam']} - "
            f"{jadwal[1]['nama']} - {jadwal[2]['nama']}"
        )

# Fungsi untuk menambah jadwal
def tambah_jadwal():
    global mata_kuliah, waktu, ruangan, dosen

    mk = input("Masukkan mata kuliah: ")
    hari = input("Masukkan hari: ")
    jam = input("Masukkan waktu (jam): ")
    ruangan_baru = input("Masukkan ruangan: ")
    dosen_baru = input("Masukkan dosen: ")
    
    print("\nDetail jadwal yang dimasukkan:")
    print(f"Mata Kuliah: {mk}")
    print(f"Hari: {hari}")
    print(f"Jam: {jam}")
    print(f"Ruangan: {ruangan_baru}")
    print(f"Dosen: {dosen_baru}")
    checked = input("Apakah jadwal sudah sesuai? (y/n): ").lower()

    if checked == "y":
        mk_kode = f"MK{len(mata_kuliah) + 1:03d}"
        waktu_kode = f"W{len(waktu) + 1:03d}"
        ruang_kode = f"R{len(ruangan) + 1:03d}"
        dosen_kode = f"D{len(dosen) + 1:03d}"

        mata_kuliah.append({"kode": mk_kode, "nama": mk})
        waktu.append({"kode": waktu_kode, "hari": hari, "jam": jam})
        ruangan.append({"kode": ruang_kode, "nama": ruangan_baru})
        dosen.append({"kode": dosen_kode, "nama": dosen_baru})
        
        print("Jadwal berhasil ditambahkan!\n")
        if input("Apakah Anda akan menambahkan jadwal lagi? (y/n): ").lower() == "y":
            tambah_jadwal()
        else:
            menu()
    else:
        print("Jadwal tidak sesuai. Silakan coba lagi.\n")
        tambah_jadwal()

# Menu
def menu():
    
    print("======PENJADWALAN OTOMATIS MENGGUNAKAN ALGORITMA GENETIKA======\n")
    print("1. Penjadwalan Otomatis")
    print("2. Tambah Jadwal Baru")
    print("3. Keluar")
    print("===============================================================\n")
    choice = input("Masukkan pilihan: ")
    if choice == "1":
        main_genetic_algorithm()
    elif choice == "2":
        tambah_jadwal()
    elif choice == "3":
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu()

menu()
