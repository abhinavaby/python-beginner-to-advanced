import qrcode


url=input("enter the url: ").strip()
file="/Users/abhinavaby/Desktop/python test/qr code msker/qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file)
print("QR CODE GENERATED")
