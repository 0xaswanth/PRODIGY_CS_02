# PRODIGY_CS_02

# Image Encryption Tool - Prodigy InfoTech Internship Task 2

## Objective
This Python program implements an **Image Encryption and Decryption** tool using pixel manipulation. The tool allows users to encrypt and decrypt images by applying a basic XOR operation on the image pixels, using a user-defined key. 

## Features
- **Image Encryption:** Encrypts an image by applying an XOR operation on each pixel with a key.
- **Image Decryption:** Decrypts the encrypted image by using the same key.
- **GUI:** A simple graphical user interface (GUI) built with Tkinter that allows users to select images for encryption and decryption, input the encryption key, and save the resulting images.

## Requirements
- **Python 3.x**
- **Pillow library** (Python Imaging Library Fork)
- **Tkinter library**

You can install Pillow with the following command:
```bash
pip install Pillow
```

## How It Works
The program performs the following steps:
1. Load the image.
2. Convert the image to RGB format.
3. Use a **seeded random number generator** to create a key stream based on the user-provided key.
4. Encrypt or decrypt the image by XORing the pixel values with the key stream.
5. Save the encrypted or decrypted image.

## How to Run
To run the program, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Aswanthkp333/PRODIGY_CS_02.git
    cd PRODIGY_CS_02
    ```

2. Install dependencies:
    ```bash
    pip install Pillow
    ```

3. Execute the Python script:
    ```bash
    python image_encryption_tool.py
    ```

4. The program will prompt you to choose between **Encrypting** or **Decrypting** an image.
   - After choosing, you will be asked to select the image.
   - Enter a key (a number between 0–255) for the encryption or decryption process.
   - Save the resulting encrypted or decrypted image.

## Sample Output

### Encrypting an Image:
```
Choose an option: Encrypt
Enter key: 123
Image encrypted and saved to: encrypted_image.png
```

### Decrypting an Image:
```
Choose an option: Decrypt
Enter key: 123
Image decrypted and saved to: decrypted_image.png
```

## Code Overview

```python
from tkinter import Tk, Label, Button, filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import os
import random

def encrypt_image(image_path, output_path, key):
    # Encryption logic
    ...

def decrypt_image(image_path, output_path, key):
    # Decryption logic
    ...

def main():
    # Tkinter GUI setup
    ...
```

## Acknowledgments
- **Prodigy InfoTech** for the opportunity to work on this task.


