import qrcode

url = "https://eholocation.github.io/merryXmassBasia/"  # ← wstaw swój link

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")   # zapis do pliku
