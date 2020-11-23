import qrcode

# Getting the inputs from the user.
backcolor = input("Write the back ground color as HEX code or color name.!\n")
fillcolor = input("Write the QR code color as HEX code or color name.!\n")
data = input("Write the data to fill the QR code.!\n")
file_name = input("Write the file name with extension(filename.extension).!\n")
try:
    # generating the Qr code.
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=3)  # Sets the version, error correction, box size, and the border.
    qr.add_data(data)  # Adds the data to the QR code.
    qr.make(fit=True)  # Fits the QR code into the box.
    img = qr.make_image(fill_color=fillcolor, back_color=backcolor)  # Sets the color.
    img.save(file_name)  # Sets the file name.
    print(f"QR code generated with the name of {file_name}")  # Prints the
except:
    print("Error while generating.Make check the color's and the file name.!")
