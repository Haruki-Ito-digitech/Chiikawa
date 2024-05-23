import qrcode
from PIL import Image
with open('qr.txt') as f:
    for line in f:
       img = qrcode.make(line)
       img.save('test.png')
       img.show()