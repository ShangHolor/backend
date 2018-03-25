from PIL import Image
from pyzbar.pyzbar import decode


# @param img_path string: The path to the image that contains a QR code
# @return x, y tuple: The position (x, y), the top-middle point of the scanned QR code
def get_qr_top(img_path):
    code = decode(Image.open(img_path))[0]
    rect = code[2]
    x = rect.left + rect.height // 2
    y = rect.top
    return x, y