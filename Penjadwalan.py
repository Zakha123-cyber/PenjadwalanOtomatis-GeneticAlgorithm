import random

# Inisialisasi parameter genetika
POP_SIZE = 50
MAX_GEN = 100
MUTATION_RATE = 0.1

# Representasi masalah
mata_kuliah = ["Matematika", "Fisika", "Kimia", "Biologi", "Algo"]
waktu = ["Senin 08:00", "Senin 10:00", "Selasa 08:00", "Selasa 10:00", "Senin 14:00"]
ruangan = ["Ruang 101", "Ruang 102"]
dosen = ["Dosen A", "Dosen B"]

# Inisialisasi populasi
def inisialisasi_populasi():
    return [[random.choice(waktu), random.choice(ruangan), random.choice(dosen)] for _ in mata_kuliah]

# Fungsi fitness
def evaluasi_fitness(jadwal):
    konflik = 0
    waktu_terpakai = set()
    for m in jadwal:
        if m[0] in waktu_terpakai:
            konflik += 1
        waktu_terpakai.add(m[0])
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
        jadwal[index] = [random.choice(waktu), random.choice(ruangan), random.choice(dosen)]
    return jadwal

# Algoritma Genetika
def main_genetic_algorithm():
    populasi = [inisialisasi_populasi() for _ in range(POP_SIZE)]

    for gen in range(MAX_GEN):
        populasi = [mutasi(child) for parent1, parent2 in zip(*[iter(seleksi(populasi))]*2) for child in crossover(parent1, parent2)]
        if evaluasi_fitness(populasi[0]) == 0:
            break

    # Output solusi terbaik
    jadwal_terbaik = populasi[0]
    for mk, jadwal in zip(mata_kuliah, jadwal_terbaik):
        print(f"{mk}: {jadwal}")

def tambah_jadwal():
    global mata_kuliah, waktu, ruangan, dosen

    mk = input("Masukkan mata kuliah: ")
    waktu_baru = input("Masukkan waktu: ")
    ruangan_baru = input("Masukkan ruangan: ")
    dosen_baru = input("Masukkan dosen: ")
    
    print("\nDetail jadwal yang dimasukkan:")
    print(f"Mata Kuliah: {mk}")
    print(f"Waktu: {waktu_baru}")
    print(f"Ruangan: {ruangan_baru}")
    print(f"Dosen: {dosen_baru}")
    cheked = input("Apakah jadwal sudah sesuai? (y/n): ").lower()

    if cheked == "y":
        mata_kuliah.append(mk)
        waktu.append(waktu_baru)
        ruangan.append(ruangan_baru)
        dosen.append(dosen_baru)
        print("Jadwal berhasil ditambahkan!\n")
        print("Apakah Anda akan menambahkan jadwal lagi? (y/n): ")
        if input().lower() == "y":
            tambah_jadwal()
        else:
            menu()
    else:
        print("Jadwal tidak sesuai. Silakan coba lagi.\n")
        tambah_jadwal()  

def menu():
    print("======PENJADWALAN OTOMATIS MENGGUNAKAN ALGORITMA GENETIKA======\n")
    print("1. Penjadwalan Otomatis")
    print("2. Tambah Jadwal Baru")
    print("2. Keluar")
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