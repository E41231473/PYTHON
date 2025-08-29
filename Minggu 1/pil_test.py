from PIL import Image

image_path = r"Minggu 1/img/Logo_Polije.png" 
img = Image.open(image_path)
img.show()

img_resized = img.resize((100, 100))
img_resized.show()
