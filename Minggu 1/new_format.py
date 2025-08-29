from PIL import Image

# Buka gambar
img = Image.open("Minggu 1/img/uno.png")

# Konversi gambar ke grayscale dan simpan
img_gray = img.convert("L")
img_gray.save("Minggu 1/output/gray_image.jpg")

# Simpan gambar dengan kompresi maksimal (khusus untuk format PNG)
img.save("Minggu 1/output/compressed_image.png", optimize=True)
