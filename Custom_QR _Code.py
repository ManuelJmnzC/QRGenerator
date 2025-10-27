import qrcode

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data('Feel good')
qr.make(fit=True)

img= qr.make_image(fill_color="yellow", back_color="black")
img.save('QR_img_codes/custom_example_qrcode.png')