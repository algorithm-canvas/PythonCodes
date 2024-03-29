from PIL import Image

img = Image.new("RGB", (100,100), color="white")
img.save("output_image.jpg")