import qrcode
import qrcode.image.svg

factory=qrcode.image.svg.SvgPathImage
img = qrcode.make('Feel good', image_factory=factory)
img.save('QR_img_codes/example_qrcode.svg')