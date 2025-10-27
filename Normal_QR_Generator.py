import qrcode

img = qrcode.make('Feel good')
img.save('QR_img_codes/example_qrcode.png')