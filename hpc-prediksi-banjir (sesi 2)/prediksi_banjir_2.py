
def prediksi_banjir(curah_hujan, tinggi_air):
    if curah_hujan < 0 or tinggi_air < 0:
        return "Data tidak valid"

    if curah_hujan >= 100 or tinggi_air >= 3:
        return "RISIKO TINGGI"
    elif curah_hujan >= 50 or tinggi_air >= 2:
        return "RISIKO SEDANG"
    else:
        return "RISIKO RENDAH"


# Contoh data simulasi
data_sungai = [
    {"lokasi": "Lokasi A", "hujan": 30, "air": 1.2},
    {"lokasi": "Lokasi B", "hujan": 70, "air": 2.3},
    {"lokasi": "Lokasi C", "hujan": 120, "air": 3.5}
]

print("SIMULASI PERINGATAN RISIKO BANJIR")
print("-" * 40)

for data in data_sungai:
    risiko = prediksi_banjir(
        data["hujan"],
        data["air"]
    )

    print(f"Lokasi: {data['lokasi']}")
    print(f"Curah hujan: {data['hujan']} mm")
    print(f"Tinggi air: {data['air']} m")
    print(f"Hasil: {risiko}")
    print("-" * 40)
