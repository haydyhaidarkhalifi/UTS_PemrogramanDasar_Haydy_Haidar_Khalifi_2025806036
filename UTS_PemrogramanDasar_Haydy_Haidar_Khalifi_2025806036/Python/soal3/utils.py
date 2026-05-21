import re
import string


def bersihkan_teks(teks: str) -> str:
    """
    Ubah ke lowercase dan hapus tanda baca.
    Contoh: 'Hello, World!' → 'hello world'
    """
    teks = teks.lower()
    teks = teks.translate(str.maketrans('', '', string.punctuation))
    return teks


def cetak_bar_ascii(kata: str, frekuensi: int, skala: int = 1):
    """
    Cetak satu baris grafik ASCII.
    Contoh: python     #########
    """
    bar = '#' * (frekuensi * skala)
    print(f"  {kata:<15} {bar}  ({frekuensi})")


def tulis_bar_ascii(kata: str, frekuensi: int, skala: int = 1) -> str:
    """Return string satu baris grafik ASCII untuk disimpan ke file."""
    bar = '#' * (frekuensi * skala)
    return f"  {kata:<15} {bar}  ({frekuensi})\n"


def hitung_vokal_konsonan(teks: str) -> tuple:
    """
    Hitung jumlah vokal dan konsonan dari seluruh teks.
    Return: (jumlah_vokal, jumlah_konsonan)
    """
    vokal = set('aiueo')
    konsonan = set('bcdfghjklmnpqrstvwxyz')

    teks_bersih = bersihkan_teks(teks)
    jml_vokal    = sum(1 for c in teks_bersih if c in vokal)
    jml_konsonan = sum(1 for c in teks_bersih if c in konsonan)

    return jml_vokal, jml_konsonan