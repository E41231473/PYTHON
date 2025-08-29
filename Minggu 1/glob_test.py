import glob

# Ambil semua gambar di folder Minggu 1/img
images = glob.glob("Minggu 1/img/*.[jp][pn]g*")

for image in images:
    print(image)

