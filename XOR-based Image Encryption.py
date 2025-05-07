from tkinter import Tk, Label, Button, filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import os
import random

def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        h, w, c = pixels.shape
        flat_pixels = pixels.reshape(-1, 3)

        # Use a seeded random generator
        rng = np.random.default_rng(seed=key)
        key_stream = rng.integers(0, 256, size=flat_pixels.shape, dtype=np.uint8)

        encrypted_flat = np.bitwise_xor(flat_pixels, key_stream)
        encrypted_pixels = encrypted_flat.reshape(h, w, 3)

        encrypted_image = Image.fromarray(encrypted_pixels)
        encrypted_image.save(output_path)
        messagebox.showinfo("Success", f"🔐 Image encrypted and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        h, w, c = pixels.shape
        flat_pixels = pixels.reshape(-1, 3)

        rng = np.random.default_rng(seed=key)
        key_stream = rng.integers(0, 256, size=flat_pixels.shape, dtype=np.uint8)

        decrypted_flat = np.bitwise_xor(flat_pixels, key_stream)
        decrypted_pixels = decrypted_flat.reshape(h, w, 3)

        decrypted_image = Image.fromarray(decrypted_pixels)
        decrypted_image.save(output_path)
        messagebox.showinfo("Success", f"🔓 Image decrypted and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

def get_key():
    try:
        key = simpledialog.askinteger("Enter Key", "Enter encryption/decryption key (0–255):", minvalue=0, maxvalue=255)
        if key is None:
            raise ValueError("No key provided")
        return key
    except Exception:
        messagebox.showerror("Invalid Key", "You must enter a valid number between 0–255.")
        return None

def choose_file_and_encrypt():
    image_path = filedialog.askopenfilename(title="Select Image to Encrypt", filetypes=[("Image files", "*.jpg *.png *.bmp")])
    if not image_path:
        return
    key = get_key()
    if key is None:
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], title="Save Encrypted Image As")
    if output_path:
        encrypt_image(image_path, output_path, key)

def choose_file_and_decrypt():
    image_path = filedialog.askopenfilename(title="Select Image to Decrypt", filetypes=[("Image files", "*.jpg *.png *.bmp")])
    if not image_path:
        return
    key = get_key()
    if key is None:
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], title="Save Decrypted Image As")
    if output_path:
        decrypt_image(image_path, output_path, key)

# === GUI Setup ===
def main():
    root = Tk()
    root.title("🔐 Image Encryptor/Decryptor")
    root.geometry("400x200")
    root.resizable(False, False)

    Label(root, text="🔐 Image Encryption/Decryption Tool", font=("Arial", 14, "bold")).pack(pady=20)

    Button(root, text="Encrypt Image", command=choose_file_and_encrypt, width=20, bg="#4CAF50", fg="white").pack(pady=10)
    Button(root, text="Decrypt Image", command=choose_file_and_decrypt, width=20, bg="#2196F3", fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
