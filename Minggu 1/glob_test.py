import glob

images = glob.glob("Minggu 1/img/*.[jp][pn]g*")

for image in images:
    print(image)

