from PIL import Image

# Buka gambar
img = Image.open("Minggu 1/img/uno.png")

# Ubah ukuran gambar
img_resized = img.resize((800, 600))  # Mengubah ukuran menjadi 800x600 piksel

# Simpan gambar yang telah diubah ukurannya
img_resized.save("Minggu 1/output/resized_image.png")
