#include "mahasiswa.h"

// =============================================
// Tampilkan menu utama
// =============================================
void tampilkanMenu() {
    printf("\n========================================\n");
    printf("   SISTEM DATA MAHASISWA UTS 2026\n");
    printf("========================================\n");
    printf("  1. Tambah Mahasiswa\n");
    printf("  2. Tampilkan Semua Data\n");
    printf("  3. Cari Mahasiswa (by NIM)\n");
    printf("  4. Hapus Mahasiswa (by NIM)\n");
    printf("  5. Simpan ke CSV\n");
    printf("  0. Keluar\n");
    printf("========================================\n");
    printf("Pilih: ");
}

int main() {
    Mahasiswa *head = NULL;  // linked list dimulai kosong
    int pilihan;
    char nama[50], nim[15];
    float tugas, uts, uas;

    printf("\n=== SELAMAT DATANG DI SISTEM DATA MAHASISWA ===\n");

    do {
        tampilkanMenu();
        scanf("%d", &pilihan);
        getchar();  // bersihkan newline dari buffer

        switch (pilihan) {

            case 1:  // Tambah mahasiswa
                printf("Nama    : "); fgets(nama, 50, stdin);
                nama[strcspn(nama, "\n")] = '\0';  // hapus newline
                printf("NIM     : "); fgets(nim, 15, stdin);
                nim[strcspn(nim, "\n")] = '\0';
                printf("Tugas   : "); scanf("%f", &tugas);
                printf("UTS     : "); scanf("%f", &uts);
                printf("UAS     : "); scanf("%f", &uas);
                getchar();
                tambahMahasiswa(&head, nama, nim, tugas, uts, uas);
                break;

            case 2:  // Tampilkan semua data
                tampilkanData(head);
                break;

            case 3:  // Cari mahasiswa
                printf("Masukkan NIM: "); fgets(nim, 15, stdin);
                nim[strcspn(nim, "\n")] = '\0';
                Mahasiswa *hasil = cariMahasiswa(head, nim);
                if (hasil) {
                    printf("\n[DITEMUKAN] %s | NIM: %s | NA: %.2f | Mutu: %s\n",
                           hasil->nama, hasil->nim,
                           hasil->nilai_akhir, hasil->mutu);
                } else {
                    printf("[INFO] Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
                }
                break;

            case 4:  // Hapus mahasiswa
                printf("Masukkan NIM yang dihapus: "); fgets(nim, 15, stdin);
                nim[strcspn(nim, "\n")] = '\0';
                hapusMahasiswa(&head, nim);
                break;

            case 5:  // Simpan ke CSV
                simpanKeCSV(head, "data_mahasiswa.csv");
                break;

            case 0:  // Keluar
                printf("\n[INFO] Program selesai. Memori dibebaskan.\n");
                break;

            default:
                printf("[ERROR] Pilihan tidak valid.\n");
        }

    } while (pilihan != 0);

    // Bebaskan seluruh memori sebelum program berakhir
    bebaskanMemori(&head);
    return 0;
}