from collections import Counter
import utils


def analisis_file(path_file: str) -> dict:
    """
    Baca dan analisis file teks.
    Return: dictionary berisi semua statistik.
    """
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            baris_list = f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File '{path_file}' tidak ditemukan!")
        return {}

    teks_lengkap = "".join(baris_list)

    # --- Hitung baris ---
    jumlah_baris = len(baris_list)

    # --- Hitung kata ---
    teks_bersih = utils.bersihkan_teks(teks_lengkap)
    kata_list   = teks_bersih.split()
    jumlah_kata = len(kata_list)

    # --- 5 kata paling sering ---
    counter = Counter(kata_list)
    top5    = counter.most_common(5)

    # --- Vokal & konsonan ---
    vokal, konsonan = utils.hitung_vokal_konsonan(teks_lengkap)

    return {
        "baris_list":    baris_list,
        "teks_lengkap":  teks_lengkap,
        "jumlah_baris":  jumlah_baris,
        "jumlah_kata":   jumlah_kata,
        "top5":          top5,
        "vokal":         vokal,
        "konsonan":      konsonan,
    }


def tampilkan_laporan(hasil: dict):
    """Cetak laporan statistik ke terminal."""
    if not hasil:
        return

    print("\n" + "=" * 45)
    print("       LAPORAN ANALISIS TEKS")
    print("=" * 45)
    print(f"  Jumlah Baris  : {hasil['jumlah_baris']}")
    print(f"  Jumlah Kata   : {hasil['jumlah_kata']}")
    print(f"  Huruf Vokal   : {hasil['vokal']}")
    print(f"  Huruf Konsonan: {hasil['konsonan']}")

    print("\n  [ 5 KATA PALING SERING MUNCUL ]\n")
    maks_frek = hasil['top5'][0][1] if hasil['top5'] else 1
    skala = max(1, 10 // maks_frek)  # normalisasi skala bar
    for kata, frek in hasil['top5']:
        utils.cetak_bar_ascii(kata, frek, skala)
    print("=" * 45 + "\n")


def simpan_laporan(hasil: dict, path_output: str):
    """Simpan laporan statistik ke file report.txt."""
    if not hasil:
        return

    maks_frek = hasil['top5'][0][1] if hasil['top5'] else 1
    skala = max(1, 10 // maks_frek)

    with open(path_output, "w", encoding="utf-8") as f:
        f.write("=" * 45 + "\n")
        f.write("       LAPORAN ANALISIS TEKS\n")
        f.write("=" * 45 + "\n")
        f.write(f"  Jumlah Baris  : {hasil['jumlah_baris']}\n")
        f.write(f"  Jumlah Kata   : {hasil['jumlah_kata']}\n")
        f.write(f"  Huruf Vokal   : {hasil['vokal']}\n")
        f.write(f"  Huruf Konsonan: {hasil['konsonan']}\n")
        f.write("\n  [ 5 KATA PALING SERING MUNCUL ]\n\n")
        for kata, frek in hasil['top5']:
            f.write(utils.tulis_bar_ascii(kata, frek, skala))
        f.write("\n" + "=" * 45 + "\n")

    print(f"[OK] Laporan disimpan ke '{path_output}'")