import converter
import json

# =============================================
# Path file input dan output
# =============================================
PATH_CSV  = "../../C/soal1/data_mahasiswa.csv"   # hasil program C Soal 1
PATH_JSON = "data_mahasiswa.json"           # output JSON yang akan dibuat


def tampilkan_json(data_json: list):
    """Tampilkan isi JSON yang sudah dibuat."""
    print("\n  [ ISI data_mahasiswa.json ]\n")
    print(json.dumps(data_json, indent=2, ensure_ascii=False))
    print()


def main():
    print("\n" + "=" * 50)
    print("  KONVERSI DATA: CSV → JSON")
    print("  (Integrasi C + Python — Soal 4)")
    print("=" * 50)

    # Langkah 1: Baca CSV dari hasil program C
    print(f"\n[1] Membaca file CSV: '{PATH_CSV}'")
    mahasiswa_list = converter.baca_csv(PATH_CSV)

    if not mahasiswa_list:
        print("[STOP] Tidak ada data yang dapat diproses.")
        return

    print(f"[OK] {len(mahasiswa_list)} data mahasiswa berhasil dibaca.\n")

    # Langkah 2: Tampilkan tabel di terminal
    print("[2] Menampilkan data:")
    converter.tampilkan_tabel(mahasiswa_list)

    # Langkah 3: Konversi ke JSON
    print("[3] Mengonversi ke JSON...")
    data_json = converter.konversi_ke_json(mahasiswa_list, PATH_JSON)

    # Langkah 4: Preview isi JSON
    tampilkan_json(data_json)

    print("  Proses integrasi CSV → JSON selesai!\n")


if __name__ == "__main__":
    main()