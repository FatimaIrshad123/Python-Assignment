#qrcode generator

import qrcode

data = 'My name is Fatima'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('D:/cohort/Python/pictures/myqrcode1.png')

# qrcode decoder

#from pyzbar.pyzbar import decode
#from PIL import Image

#img = Image.open('D:/cohort/Python/pictures/myqrcode1.png')

#result = decode(img)
#print(result)

