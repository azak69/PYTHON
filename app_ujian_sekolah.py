def ambil_soal():
    soal_real = []
    with open("bank_soal.txt", encoding="utf-8") as file:
        for line in file:
            soal_real.append(line.strip())
    return soal_real

def buat_soal():
    soal_real = ambil_soal()

    import random
    random.shuffle(soal_real)

    soal_ujian = []
    for i in range(10):
        soal = soal_real[1]
        data = soal.split("|")
        pertanyaan = data[0]
        semua_jawaban = data[1]
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]

        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar,
        })

    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()

    jawaban_benar = 0
    jawaban_salah = 0

    for j in range(len(soal_ujian)):
        soal = soal_ujian[j]
        opsi = ["A", "B", "C", "D"]
        print("Pertanyaan", j + 1, ".", soal["pertanyaan"])
        print("Jawaban : ")

        for k in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][k]
            print(opsi[k], ".", jawaban)

        jawaban_user = input("Jawaban (A/B/C/D): ")
        jawaban_index_user = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_index_user]

        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban Benar!")
            jawaban_benar += 1
        else:
            print("Jawaban Salah!")
            jawaban_salah += 1

    print("Hasil Ujian :")
    print("Jawaban Benar : ", jawaban_benar)
    print("Jawaban Salah : ", jawaban_salah)
    print("Nilai Ujian : ", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")

app_ujian()

# Program ini adalah aplikasi ujian sekolah sederhana yang mengambil soal dari file teks, mengacak soal dan jawaban, serta menghitung hasil ujian berdasarkan jawaban pengguna.
# Buatlah file teks bernama "bank_soal.txt" dengan format soal yang sesuai agar program dapat berjalan dengan baik.
# Format soal dalam file teks adalah sebagai berikut:Pertanyaan|Jawaban1,Jawaaban2,Jawaaban3,Jawaaban4