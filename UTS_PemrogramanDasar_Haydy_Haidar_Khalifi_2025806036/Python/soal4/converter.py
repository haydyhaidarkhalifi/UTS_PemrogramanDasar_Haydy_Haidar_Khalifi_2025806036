import csv
import json
import os


def baca_csv(path_csv: str) -> list:
    """
    Baca file CSV hasil program C dan kembalikan sebagai list of dict.
    Return: list berisi dict tiap mahasiswa, atau [] jika gagal.
    """
    if not os.path.exists(path_csv):
        print(f"[ERROR] File '{path_csv}' tidak ditemukan!")
        print("  Pastikan program C (Soal 1) sudah dijalankan dan menghasilkan CSV.")
        return []

    mahasiswa_list = []

    with open(path_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # baca otomatis pakai header baris pertama
        for baris in reader:
            try:
                # Konversi tipe data sesuai kebutuhan
                mahasiswa = {
                    "nama":        baris["Nama"].strip(),
                    "nim":         baris["NIM"].strip(),
                    "tugas":       float(baris["Tugas"]),
                    "uts":         float(baris["UTS"]),
                    "uas":         float(baris["UAS"]),
                    "nilai_akhir": float(baris["NilaiAkhir"]),
                    "mutu":        baris["Mutu"].strip(),
                }
                mahasiswa_list.append(mahasiswa)
            except (KeyError, ValueError) as e:
                print(f"[WARNING] Baris tidak valid dilewati: {e}")

    return mahasiswa_list


def hitung_rata_rata(mahasiswa_list: list) -> float:
    """Hitung rata-rata nilai akhir semua mahasiswa."""
    if not mahasiswa_list:
        return 0.0
    total = sum(m["nilai_akhir"] for m in mahasiswa_list)
    return total / len(mahasiswa_list)


def tampilkan_tabel(mahasiswa_list: list):
    """Tampilkan data mahasiswa dalam format tabel rapi."""
    if not mahasiswa_list:
        print("  Tidak ada data untuk ditampilkan.")
        return

    print("\n" + "=" * 70)
    print("  DATA MAHASISWA (dibaca dari CSV)")
    print("=" * 70)
    print(f"  {'Nama':<20} {'NIM':<12} {'Tugas':>6} {'UTS':>6} {'UAS':>6} {'NA':>7} {'Mutu':>5}")
    print(f"  {'-'*20} {'-'*12} {'-'*6} {'-'*6} {'-'*6} {'-'*7} {'-'*5}")

    for m in mahasiswa_list:
        print(f"  {m['nama']:<20} {m['nim']:<12} "
              f"{m['tugas']:>6.2f} {m['uts']:>6.2f} {m['uas']:>6.2f} "
              f"{m['nilai_akhir']:>7.2f} {m['mutu']:>5}")

    rata = hitung_rata_rata(mahasiswa_list)
    print("=" * 70)
    print(f"  Rata-rata Nilai Akhir: {rata:.2f}")
    print("=" * 70 + "\n")


def konversi_ke_json(mahasiswa_list: list, path_json: str):
    """
    Simpan data mahasiswa ke file JSON.
    Format JSON: list of dict dengan field nama, nim, nilai_akhir, mutu.
    """
    # Hanya simpan field yang relevan ke JSON (sesuai instruksi soal)
    data_json = [
        {
            "nama":        m["nama"],
            "nim":         m["nim"],
            "nilai_akhir": m["nilai_akhir"],
            "mutu":        m["mutu"]
        }
        for m in mahasiswa_list
    ]

    with open(path_json, "w", encoding="utf-8") as f:
        json.dump(data_json, f, indent=2, ensure_ascii=False)

    print(f"[OK] Data berhasil dikonversi ke '{path_json}'")
    return data_json