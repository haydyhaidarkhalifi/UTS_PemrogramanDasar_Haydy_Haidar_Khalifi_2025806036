#ifndef MAHASISWA_H
#define MAHASISWA_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// =============================================
// STRUCT: Node linked list data mahasiswa
// =============================================
typedef struct Mahasiswa {
    char nama[50];
    char nim[15];
    float nilai_tugas;
    float nilai_uts;
    float nilai_uas;
    float nilai_akhir;
    char mutu[3];
    struct Mahasiswa *next;  // pointer ke node berikutnya
} Mahasiswa;

// =============================================
// PROTOTIPE FUNGSI
// =============================================
float hitungNilaiAkhir(float tugas, float uts, float uas);
void tentukanMutu(float nilai_akhir, char *mutu);
void tambahMahasiswa(Mahasiswa **head, char *nama, char *nim,
                     float tugas, float uts, float uas);
Mahasiswa* cariMahasiswa(Mahasiswa *head, char *nim);
void hapusMahasiswa(Mahasiswa **head, char *nim);
void tampilkanData(Mahasiswa *head);
void simpanKeCSV(Mahasiswa *head, const char *namaFile);
void bebaskanMemori(Mahasiswa **head);

#endif