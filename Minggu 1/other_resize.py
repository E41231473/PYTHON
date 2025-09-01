from PIL import Image

img = Image.open("Minggu 1/img/uno.png")

img_resized = img.resize((800, 600))

img_resized.save("Minggu 1/output/resized_image.png")
