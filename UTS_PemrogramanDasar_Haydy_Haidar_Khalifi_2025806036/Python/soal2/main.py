from colorama import Fore, Style, init
import game
import scoreboard

init(autoreset=True)


def tampilkan_banner():
    print(Fore.CYAN + """
  ╔══════════════════════════════════╗
  ║        GUESS BATTLE GAME         ║
  ║   Multi-Level & Multi-Player     ║
  ╚══════════════════════════════════╝
    """)


def menu_level() -> int:
    """Tampilkan pilihan level dan return pilihan user."""
    print("  Pilih Level:")
    print("    1. Level 1 — Angka 1–10  (3 percobaan)")
    print("    2. Level 2 — Angka 1–50  (5 percobaan)")
    print("    3. Level 3 — Angka 1–100 (7 percobaan)")
    print("    0. Lihat Scoreboard & Keluar")

    while True:
        try:
            pilihan = int(input("\n  Pilih (0-3): "))
            if pilihan in [0, 1, 2, 3]:
                return pilihan
            print("  [ERROR] Pilihan tidak valid.")
        except ValueError:
            print("  [ERROR] Masukkan angka!")


def main():
    tampilkan_banner()

    # Login: minta nama pemain
    nama = input("  Masukkan nama kamu: ").strip()
    if not nama:
        nama = "Anonim"

    # Cek apakah pemain sudah pernah main
    data = scoreboard.muat_skor()
    if nama in data:
        print(Fore.YELLOW + f"\n  Selamat datang kembali, {nama}! Skor kamu: {data[nama]} pts")
    else:
        print(Fore.GREEN + f"\n  Halo, {nama}! Ini pertama kali kamu bermain.")

    total_poin_sesi = 0

    # Loop game
    while True:
        pilihan = menu_level()

        if pilihan == 0:
            break  # keluar ke scoreboard

        # Mainkan level yang dipilih
        poin = game.mainkan_level(pilihan)
        total_poin_sesi += poin

        if poin > 0:
            # Update skor ke JSON
            skor_baru = scoreboard.update_skor(nama, poin)
            print(Fore.GREEN + f"  Total skor kamu sekarang: {skor_baru} pts")

        lanjut = input("  Main lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    print(f"\n  Kamu mendapat {total_poin_sesi} poin di sesi ini.")
    scoreboard.tampilkan_top5()
    print(Fore.CYAN + "  Terima kasih sudah bermain! Sampai jumpa!\n")


if __name__ == "__main__":
    main()