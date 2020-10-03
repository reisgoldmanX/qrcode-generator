import qrcode

qr = qrcode.QRCode(
    version=1,                                             #bigger the value more data ! lower the value less data 1
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=18,                                           #Clasic size 15
    border=3                                          #Clasic Border 5
    )
data = "<The data you want to put(URL, TEXT>"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color= "black") #back_color equals to background color. fill_color equals to inside color.
img.save("<FİLE_NAME>.PNG")