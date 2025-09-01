from PIL import Image

img = Image.open("Minggu 1/img/uno.png")

img_gray = img.convert("L")
img_gray.save("Minggu 1/output/gray_image.jpg")

img.save("Minggu 1/output/compressed_image.png", optimize=True)
