import argparse
import analyzer


def main():
    # Argparse: mendukung parameter CLI
    parser = argparse.ArgumentParser(description="Analisis Teks Otomatis")
    parser.add_argument(
        "--file",
        type=str,
        default="input.txt",
        help="Path file teks yang akan dianalisis (default: input.txt)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="report.txt",
        help="Path file laporan output (default: report.txt)"
    )
    args = parser.parse_args()

    print(f"\n[INFO] Menganalisis file: '{args.file}'")

    # Jalankan analisis
    hasil = analyzer.analisis_file(args.file)

    if hasil:
        # Tampilkan ke terminal
        analyzer.tampilkan_laporan(hasil)
        # Simpan ke file
        analyzer.simpan_laporan(hasil, args.output)


if __name__ == "__main__":
    main()