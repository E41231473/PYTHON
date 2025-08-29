from PIL import Image

img = Image.open("Minggu 1/img/uno.png")

img.save("Minggu 1/output/image.png")

img.save("Minggu 1/output/new_image.png")

img.save("Minggu 1/output/image_quality.png", quality=85)
