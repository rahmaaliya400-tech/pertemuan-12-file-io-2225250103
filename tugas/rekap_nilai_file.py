
def baca_dan_validasi_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data_nilai.append((nim, nilai))
                except ValueError:
                    print(f"Data tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print("File nilai tidak ditemukan.")

    return data_nilai


def tulis_hasil_rekap(nama_file, data_nilai):
    with open(nama_file, "w", encoding="utf-8") as file:
        if not data_nilai:
            file.write("Tidak ada data nilai yang valid.\n")
            return

        jumlah_data = len(data_nilai)
        total_nilai = sum(nilai for nim, nilai in data_nilai)
        rata_rata = total_nilai / jumlah_data
        nilai_min = min(nilai for nim, nilai in data_nilai)
        nilai_max = max(nilai for nim, nilai in data_nilai)
        jumlah_lulus = sum(
            1 for nim, nilai in data_nilai if nilai >= 60
        )

        file.write("HASIL REKAP NILAI\n")
        file.write("=================\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_min:.2f}\n")
        file.write(f"Nilai maksimum: {nilai_max:.2f}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")


data_nilai = baca_dan_validasi_nilai("data/nilai.txt")
tulis_hasil_rekap("data/hasil_rekap.txt", data_nilai)

print("Rekap nilai berhasil dibuat.")
