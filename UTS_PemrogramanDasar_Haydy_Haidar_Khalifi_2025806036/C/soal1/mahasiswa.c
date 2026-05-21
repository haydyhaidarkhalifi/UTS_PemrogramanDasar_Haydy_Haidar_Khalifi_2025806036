#include "mahasiswa.h"

// =============================================
// Hitung nilai akhir: 30% tugas + 30% UTS + 40% UAS
// =============================================
float hitungNilaiAkhir(float tugas, float uts, float uas) {
    return (0.30f * tugas) + (0.30f * uts) + (0.40f * uas);
}

// =============================================
// Tentukan huruf mutu berdasarkan nilai akhir
// =============================================
void tentukanMutu(float nilai_akhir, char *mutu) {
    if (nilai_akhir >= 85)       strcpy(mutu, "A");
    else if (nilai_akhir >= 75)  strcpy(mutu, "B");
    else if (nilai_akhir >= 60)  strcpy(mutu, "C");
    else if (nilai_akhir >= 50)  strcpy(mutu, "D");
    else                          strcpy(mutu, "E");
}

// =============================================
// Tambah mahasiswa baru ke linked list (di depan)
// =============================================
void tambahMahasiswa(Mahasiswa **head, char *nama, char *nim,
                     float tugas, float uts, float uas) {
    // Alokasi memori dinamis untuk node baru
    Mahasiswa *baru = (Mahasiswa *)malloc(sizeof(Mahasiswa));
    if (baru == NULL) {
        printf("[ERROR] Gagal alokasi memori!\n");
        return;
    }

    // Isi data mahasiswa
    strcpy(baru->nama, nama);
    strcpy(baru->nim, nim);
    baru->nilai_tugas = tugas;
    baru->nilai_uts   = uts;
    baru->nilai_uas   = uas;
    baru->nilai_akhir = hitungNilaiAkhir(tugas, uts, uas);
    tentukanMutu(baru->nilai_akhir, baru->mutu);
    baru->next = *head;  // sambungkan ke node lama

    *head = baru;  // head sekarang menunjuk node baru
    printf("[OK] Mahasiswa '%s' berhasil ditambahkan.\n", nama);
}

// =============================================
// Cari mahasiswa berdasarkan NIM
// =============================================
Mahasiswa* cariMahasiswa(Mahasiswa *head, char *nim) {
    Mahasiswa *temp = head;
    while (temp != NULL) {
        if (strcmp(temp->nim, nim) == 0) {
            return temp;  // ditemukan
        }
        temp = temp->next;
    }
    return NULL;  // tidak ditemukan
}

// =============================================
// Hapus mahasiswa berdasarkan NIM + free memori
// =============================================
void hapusMahasiswa(Mahasiswa **head, char *nim) {
    Mahasiswa *temp = *head;
    Mahasiswa *prev = NULL;

    // Cari node yang cocok
    while (temp != NULL && strcmp(temp->nim, nim) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("[INFO] Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
        return;
    }

    // Putuskan node dari linked list
    if (prev == NULL) {
        *head = temp->next;  // hapus node pertama
    } else {
        prev->next = temp->next;
    }

    printf("[OK] Mahasiswa '%s' (NIM: %s) dihapus.\n", temp->nama, temp->nim);
    free(temp);  // WAJIB bebaskan memori
}

// =============================================
// Tampilkan semua data dalam format tabel
// =============================================
void tampilkanData(Mahasiswa *head) {
    if (head == NULL) {
        printf("[INFO] Data mahasiswa kosong.\n");
        return;
    }

    printf("\n");
    printf("%-20s %-12s %7s %7s %7s %11s %6s\n",
           "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir", "Mutu");
    printf("%-20s %-12s %7s %7s %7s %11s %6s\n",
           "--------------------", "------------",
           "-------", "-------", "-------", "-----------", "------");

    Mahasiswa *temp = head;
    while (temp != NULL) {
        printf("%-20s %-12s %7.2f %7.2f %7.2f %11.2f %6s\n",
               temp->nama, temp->nim,
               temp->nilai_tugas, temp->nilai_uts, temp->nilai_uas,
               temp->nilai_akhir, temp->mutu);
        temp = temp->next;
    }
    printf("\n");
}

// =============================================
// Simpan semua data ke file CSV
// =============================================
void simpanKeCSV(Mahasiswa *head, const char *namaFile) {
    FILE *fp = fopen(namaFile, "w");
    if (fp == NULL) {
        printf("[ERROR] Gagal membuka file '%s'\n", namaFile);
        return;
    }

    // Tulis header CSV
    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    // Tulis setiap record
    Mahasiswa *temp = head;
    while (temp != NULL) {
        fprintf(fp, "%s,%s,%.2f,%.2f,%.2f,%.2f,%s\n",
                temp->nama, temp->nim,
                temp->nilai_tugas, temp->nilai_uts, temp->nilai_uas,
                temp->nilai_akhir, temp->mutu);
        temp = temp->next;
    }

    fclose(fp);
    printf("[OK] Data berhasil disimpan ke '%s'\n", namaFile);
}

// =============================================
// Bebaskan seluruh memori linked list
// =============================================
void bebaskanMemori(Mahasiswa **head) {
    Mahasiswa *temp;
    while (*head != NULL) {
        temp = *head;
        *head = (*head)->next;
        free(temp);
    }
}