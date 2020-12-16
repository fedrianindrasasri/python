# membuat dictionary
skill_saya = {
    "utama": "PHP",
    "lainnya": ["Java", "Javascript", "python", "GO"]
}
# cetak isi utama
print(skill_saya["utama"])

# ubah isi utama
skill_saya["utama"] = "VB.NET"

# cetak lagi
print(skill_saya["utama"])


# hapus dengan del
del skill_saya["utama"]
print(skill_saya)

# hapus dengan pop
# skill_saya.pop("utama")
