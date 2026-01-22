import qrcode
from PIL import Image

data = input("enter a thing: ")
qr = qrcode.QRCode(version=3, box_size=8, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")

image.save("qr4_code.png")
Image.open("qr4_code.png")