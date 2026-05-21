import json
import os

SCORE_FILE = "scores.json"


def muat_skor():
    """Muat data skor dari file JSON. Buat baru jika belum ada."""
    if not os.path.exists(SCORE_FILE):
        return {}
    with open(SCORE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def simpan_skor(data: dict):
    """Simpan seluruh data skor ke file JSON."""
    with open(SCORE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def update_skor(nama: str, poin: int):
    """Tambahkan poin ke skor pemain. Jika pemain baru, buat entri."""
    data = muat_skor()
    if nama in data:
        data[nama] += poin
    else:
        data[nama] = poin
    simpan_skor(data)
    return data[nama]


def tampilkan_top5():
    """Tampilkan 5 besar pemain dengan skor tertinggi."""
    data = muat_skor()
    if not data:
        print("  Belum ada data skor.")
        return

    # Urutkan dari skor terbesar
    urutan = sorted(data.items(), key=lambda x: x[1], reverse=True)

    print("\n  ╔══════════════════════════╗")
    print("  ║      TOP 5 SCORE         ║")
    print("  ╠══════════════════════════╣")
    for i, (nama, skor) in enumerate(urutan[:5], start=1):
        print(f"  ║  {i}. {nama:<15} {skor:>5} pts ║")
    print("  ╚══════════════════════════╝\n")