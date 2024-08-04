import pyqrcode

t = input("Type your text ==> ")

# Create the QR code
qr_code = pyqrcode.create(t)  # No need to encode here

# Save the QR code as an image
file_name = "QR.png"
qr_code.png(file_name, scale=5)
print(f"QR code saved as {file_name}")
