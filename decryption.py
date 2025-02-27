import cv2
import os
import string

# Read the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct image path

# Dictionaries for decoding
c = {i: chr(i) for i in range(256)}

# Decryption process
message = ""
m, n = 0, 0

# Define the password used during encryption
password = "1234"  # The password used during encryption
pas = input("Enter passcode for Decryption: ")

# Define the length of the message
msg_length = int(input("Enter the length of the encrypted message: "))

if password == pas:
    for i in range(msg_length):
        if m >= img.shape[1]:
            m = 0
            n += 1
        if n >= img.shape[0]:
            break
        message += c[img[n, m][0]]  # Only read one channel
        m += 1
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")



