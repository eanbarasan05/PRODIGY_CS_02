# 🔐 Image Encryption System

<div align="center">

### Secure Digital Images Using Advanced Pixel Manipulation Techniques

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-orange?style=for-the-badge\&logo=numpy)
![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-green?style=for-the-badge)


</div>

---

## 📖 Overview

The **Image Encryption System** is a Python-based cybersecurity application designed to protect digital images through advanced pixel manipulation techniques.

The system supports both **Single-Layer** and **Multi-Layer Encryption**, allowing users to encrypt and decrypt images using multiple security algorithms and user-defined secret keys.

This project demonstrates fundamental concepts of:

* 🔒 Image Encryption
* 🔑 Symmetric Cryptography
* 🖼️ Image Processing
* 🔄 Pixel Manipulation
* 🛡️ Data Protection Techniques

---

## ✨ Features

### 🔹 Single-Layer Encryption

Encrypt or decrypt images using a single algorithm:

* XOR Encryption
* ADD Encryption (Modular Arithmetic)
* SWAP Encryption (Pixel Shuffling)

### 🔹 Multi-Layer Encryption

Apply multiple encryption algorithms sequentially for enhanced security.

Available combinations:

| Combination | Sequence         |
| ----------- | ---------------- |
| Layer 1     | XOR → ADD → SWAP |
| Layer 2     | ADD → XOR → SWAP |
| Layer 3     | SWAP → XOR → ADD |

### 🚀 Additional Features

✔ RGB Image Support

✔ Encryption & Decryption

✔ User-Defined Secret Keys

✔ Menu-Driven Interface

✔ Automatic Output Generation

✔ Multiple Image Format Support

✔ Fast Processing Using NumPy

---

## 🛠️ Technologies Used

| Technology    | Purpose            |
| ------------- | ------------------ |
| Python 3.x    | Core Programming   |
| Pillow (PIL)  | Image Processing   |
| NumPy         | Pixel Manipulation |
| Random Module | Pixel Shuffling    |

---

## 📂 Project Structure

```text
Image-Encryption-System/
│
├── image_encryptor.py
├── README.md
├── requirements.txt
│
└── sample_images/
    ├── original_image.jpg
    ├── encrypted_image.png
    └── decrypted_image.png
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/eanbarasan05/PRODIGY_CS_02.git Image-Encryption-System
cd Image-Encryption-System
```

### Install Required Libraries

```bash
pip install pillow numpy
```

Or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python image_encryptor.py
```

---

## 🖥️ Application Workflow

### Main Menu

```text
=========================================
IMAGE ENCRYPTION SYSTEM
=========================================

Encryption Mode:
1. Single Layer Encryption & Decryption
2. Multi Layer Encryption & Decryption
3. Exit
```

### Single Layer Encryption

```text
1. Encrypt Image
2. Decrypt Image
3. Back

Encryption Types:
1. XOR Encryption
2. ADD Encryption
3. SWAP Encryption
```

### Multi Layer Encryption

```text
1. Encrypt Image
2. Decrypt Image
3. Back

Layer Combinations:
1. XOR → ADD → SWAP
2. ADD → XOR → SWAP
3. SWAP → XOR → ADD
```

---

## 🔐 Encryption Algorithms

### 1️⃣ XOR Encryption

Each pixel value is XORed with a secret key.

```text
Encrypted Pixel = Pixel XOR Key
```

Decryption is performed using the same operation.

---

### 2️⃣ ADD Encryption

Adds a secret key to every pixel channel using modulo arithmetic.

```text
Encrypted Pixel = (Pixel + Key) mod 256
```

Decryption:

```text
Original Pixel = (Encrypted Pixel - Key) mod 256
```

---

### 3️⃣ SWAP Encryption

Randomly shuffles pixel positions using a key-generated sequence.

```text
Original Pixels → Shuffle → Encrypted Image
```

The same key restores the original image.

---

## 🔥 Multi-Layer Security

Multi-layer encryption combines multiple algorithms to increase security.

### Example

```text
Original Image
      │
      ▼
 XOR Encryption
      │
      ▼
 ADD Encryption
      │
      ▼
 SWAP Encryption
      │
      ▼
 Encrypted Image
```

Decryption performs the reverse sequence.

---

## 📸 Sample Output

### Encryption

```text
Choose: 1

Enter image path: sample.jpg

Encryption Types:
1. XOR Encryption
2. ADD Encryption
3. SWAP Encryption

Choose Type: 1
Enter Key: 50

[+] Saved: sample_encrypted.png
```

### Decryption

```text
Choose: 2

Enter image path: sample_encrypted.png

Choose Type: 1
Enter Key: 50

[+] Saved: sample_decrypted.png
```

---

## 🎯 Learning Outcomes

This project helped in understanding:

* Image Processing Fundamentals
* Pixel-Level Data Manipulation
* Symmetric Encryption Techniques
* Modular Arithmetic
* Randomized Transformations
* Cyber Security Concepts
* Python Development

---

## 🚀 Future Enhancements

* Password-Based Key Generation
* SHA-256 Integrity Verification
* AES Image Encryption
* GUI with Tkinter
* Batch Image Encryption
* Drag & Drop Interface
* Encryption Logs
* Histogram Analysis
* Encryption Strength Metrics

---

## 👨‍💻 Author

### ANBARASAN E

**Cyber Security Intern**
**Prodigy Infotech**

---

## 📌 Internship Task Information

**Task 02:** Pixel Manipulation for Image Encryption

**Domain:** Cyber Security

**Organization:** Prodigy Infotech

**Objective:** Develop a secure image encryption and decryption tool using pixel manipulation techniques such as pixel value modification and pixel position transformation.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star ⭐

#ProdigyInfotech #CyberSecurity #Python #ImageEncryption #Cryptography #InternshipProject

</div>
