from PIL import Image,ImageOps
import sys

if len(sys.argv) < 3:
    sys,exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[-2].endswith((".jpg",".jpeg")):
    sys.exit("Invalid input")

try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    input_w,input_l = image.size
    target_size = (int(input_w*0.8),int(input_l*0.8))
    fit_shirt = ImageOps.fit(shirt,size=target_size,method=Image.Resampling.LANCZOS,centering=(0.5,1))
    offset_x = int(input_w*0.1)
    offset_y = int(0.2*input_l)
    image.paste(fit_shirt,(offset_x,offset_y),fit_shirt) #from the upper left corner
    image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not exist.")
