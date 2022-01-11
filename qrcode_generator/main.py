import qrcode

from pyzbar.pyzbar import decode
from PIL import Image

def image_decode(img):
    img_code = Image.open(img)
    decode_message = decode(img_code)
    print(decode_message)

def image_encode(data):
    #optimize the created qr code
    #Version parameter is an integer from 1 to 40
    # using version we can control the size of the QR code version 1 is smallest
    #you can also set it as none and fit to fit automatically
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="red",back_color="black")
    qr_img.save("qrcode3.jpg")
    print("Qr code created")

data = "https://anuptechtips.com"
img = "qrcode.png"

image_decode(img)
image_encode(data)

