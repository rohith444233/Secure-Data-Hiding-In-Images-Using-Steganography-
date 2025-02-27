import cv2
import os

# Read the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save the password to a file
with open("password.txt", "w") as f:
    f.write(password)

# Embed the message into the image
m, n, z = 0, 0, 0
for char in msg:
    img[n, m, z] = ord(char)
    z = (z + 1) % 3
    if z == 0:
        m = (m + 1) % img.shape[1]
        n = (n + 1) % img.shape[0]

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

print("Message encrypted successfully!")

