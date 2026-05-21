import random
from colorama import Fore, Style, init

# Inisialisasi colorama (agar warna bekerja di Windows juga)
init(autoreset=True)

# Konfigurasi tiap level: (rentang_max, max_percobaan, faktor_skor)
LEVEL_CONFIG = {
    1: {"max": 10,  "percobaan": 3,  "faktor": 30},
    2: {"max": 50,  "percobaan": 5,  "faktor": 20},
    3: {"max": 100, "percobaan": 7,  "faktor": 15},
}


def hitung_skor(sisa_percobaan: int, faktor: int) -> int:
    """Hitung skor berdasarkan sisa percobaan × faktor level."""
    return sisa_percobaan * faktor


def mainkan_level(level: int) -> int:
    """
    Jalankan satu sesi permainan untuk level tertentu.
    Return: poin yang didapat (0 jika kalah)
    """
    config = LEVEL_CONFIG[level]
    batas  = config["max"]
    maks   = config["percobaan"]
    faktor = config["faktor"]

    angka_rahasia = random.randint(1, batas)
    sisa = maks

    print(Fore.CYAN + f"\n  [ LEVEL {level} ] Tebak angka antara 1 – {batas}")
    print(f"  Kamu punya {maks} percobaan.\n")

    while sisa > 0:
        print(f"  Sisa percobaan: {Fore.YELLOW}{sisa}")
        tebakan_raw = input("  Tebakan kamu: ").strip()

        # Error handling jika bukan angka
        try:
            tebakan = int(tebakan_raw)
        except ValueError:
            print(Fore.RED + "  [ERROR] Masukkan angka yang valid!")
            continue

        sisa -= 1

        if tebakan == angka_rahasia:
            poin = hitung_skor(sisa, faktor)
            print(Fore.GREEN + f"\n  ✅ BENAR! Angkanya memang {angka_rahasia}!")
            print(Fore.GREEN + f"  🏆 Kamu mendapat {poin} poin!\n")
            return poin
        elif tebakan < angka_rahasia:
            print(Fore.RED + "  ⬆  Terlalu kecil! Coba lebih besar.\n")
        else:
            print(Fore.RED + "  ⬇  Terlalu besar! Coba lebih kecil.\n")

    # Gagal semua percobaan
    print(Fore.RED + f"\n  ❌ Kamu kehabisan percobaan! Angkanya adalah {angka_rahasia}.\n")
    return 0