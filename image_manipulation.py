import cv2
import numpy as np

def encrypt_image(image_path, output_path, swap_pixels=True, xor_key=100):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not read image.")
        return

    height, width, channels = img.shape

    if swap_pixels:
        # Swap pixel values horizontally
        for i in range(height):
            for j in range(0, width, 2):
                img[i][j], img[i][j + 1] = img[i][j + 1], img[i][j]

    # Apply XOR operation with the key
    img = cv2.bitwise_xor(img, xor_key)

    cv2.imwrite(output_path, img)
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, output_path, swap_pixels=True, xor_key=100):
    encrypted_img = cv2.imread(encrypted_image_path)

    if encrypted_img is None:
        print("Error: Could not read encrypted image.")
        return

    height, width, channels = encrypted_img.shape

    # Reverse XOR operation
    decrypted_img = cv2.bitwise_xor(encrypted_img, xor_key)

    if swap_pixels:
        # Reverse pixel swapping
        for i in range(height):
            for j in range(0, width, 2):
                decrypted_img[i][j], decrypted_img[i][j + 1] = decrypted_img[i][j + 1], decrypted_img[i][j]

    cv2.imwrite(output_path, decrypted_img)
    print("Image decrypted successfully.")

if __name__ == "__main__":
    image_path = "my_image.jpg"
    encrypted_image_path = "encrypted_image.jpg"
    decrypted_image_path = "decrypted_image.jpg"

    # Encrypt the image
    encrypt_image(image_path, encrypted_image_path)

    # Decrypt the encrypted image
    decrypt_image(encrypted_image_path, decrypted_image_path)