from PIL import Image
import numpy as np
import random
import os


# ==========================================================
# IMAGE UTILITIES
# ==========================================================

def load_image(path):
    img = Image.open(path).convert("RGB")
    return np.array(img)


def save_image(img_array, output_path):
    Image.fromarray(img_array).save(output_path)
    print(f"\n[+] Saved: {output_path}")


# ==========================================================
# XOR
# ==========================================================

def xor_operation(img_array, key):
    return (img_array ^ key).astype(np.uint8)


# ==========================================================
# ADD
# ==========================================================

def add_encrypt(img_array, key):
    return ((img_array.astype(np.int32) + key) % 256).astype(np.uint8)


def add_decrypt(img_array, key):
    return ((img_array.astype(np.int32) - key) % 256).astype(np.uint8)


# ==========================================================
# SWAP
# ==========================================================

def swap_encrypt(img_array, key):

    flat = img_array.reshape(-1, 3).copy()

    indices = list(range(len(flat)))

    random.seed(key)
    random.shuffle(indices)

    encrypted = flat[indices]

    return encrypted.reshape(img_array.shape)


def swap_decrypt(img_array, key):

    flat = img_array.reshape(-1, 3).copy()

    indices = list(range(len(flat)))

    random.seed(key)
    random.shuffle(indices)

    original = np.empty_like(flat)

    for i, shuffled_pos in enumerate(indices):
        original[shuffled_pos] = flat[i]

    return original.reshape(img_array.shape)


# ==========================================================
# SINGLE LAYER
# ==========================================================

def single_encrypt(img_array, method, key):

    if method == 1:
        return xor_operation(img_array, key)

    elif method == 2:
        return add_encrypt(img_array, key)

    elif method == 3:
        return swap_encrypt(img_array, key)


def single_decrypt(img_array, method, key):

    if method == 1:
        return xor_operation(img_array, key)

    elif method == 2:
        return add_decrypt(img_array, key)

    elif method == 3:
        return swap_decrypt(img_array, key)


# ==========================================================
# MULTI LAYER
# ==========================================================

def multilayer_encrypt(img_array, layer_choice, k1, k2, k3):

    if layer_choice == 1:
        img_array = xor_operation(img_array, k1)
        img_array = add_encrypt(img_array, k2)
        img_array = swap_encrypt(img_array, k3)

    elif layer_choice == 2:
        img_array = add_encrypt(img_array, k1)
        img_array = xor_operation(img_array, k2)
        img_array = swap_encrypt(img_array, k3)

    elif layer_choice == 3:
        img_array = swap_encrypt(img_array, k1)
        img_array = xor_operation(img_array, k2)
        img_array = add_encrypt(img_array, k3)

    return img_array


def multilayer_decrypt(img_array, layer_choice, k1, k2, k3):

    if layer_choice == 1:
        img_array = swap_decrypt(img_array, k3)
        img_array = add_decrypt(img_array, k2)
        img_array = xor_operation(img_array, k1)

    elif layer_choice == 2:
        img_array = swap_decrypt(img_array, k3)
        img_array = xor_operation(img_array, k2)
        img_array = add_decrypt(img_array, k1)

    elif layer_choice == 3:
        img_array = add_decrypt(img_array, k3)
        img_array = xor_operation(img_array, k2)
        img_array = swap_decrypt(img_array, k1)

    return img_array


# ==========================================================
# MENUS
# ==========================================================

def banner():
    print("\n" + "=" * 45)
    print("      IMAGE ENCRYPTION SYSTEM")
    print("=" * 45)


def get_path():

    path = input("\nEnter image path: ").strip()

    if not os.path.exists(path):
        print("[-] File not found!")
        return None

    return path


# ==========================================================
# SINGLE LAYER MENU
# ==========================================================

def single_layer_menu():

    while True:

        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Back")

        choice = input("\nChoose: ")

        if choice == "3":
            break

        path = get_path()

        if not path:
            continue

        img = load_image(path)

        print("\nEncryption Types")
        print("1. XOR Encryption")
        print("2. ADD Encryption")
        print("3. SWAP Encryption")

        method = int(input("\nChoose Type: "))
        key = int(input("Enter Key: "))

        if choice == "1":
            result = single_encrypt(img, method, key)
            out = path.rsplit(".", 1)[0] + "_encrypted.png"

        else:
            result = single_decrypt(img, method, key)
            out = path.rsplit(".", 1)[0] + "_decrypted.png"

        save_image(result, out)


# ==========================================================
# MULTI LAYER MENU
# ==========================================================

def multi_layer_menu():

    while True:

        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Back")

        choice = input("\nChoose: ")

        if choice == "3":
            break

        path = get_path()

        if not path:
            continue

        img = load_image(path)

        print("\nLayer Combinations")

        print("1. XOR -> ADD -> SWAP")
        print("2. ADD -> XOR -> SWAP")
        print("3. SWAP -> XOR -> ADD")

        layer_choice = int(input("\nChoose Combination: "))

        print("\nEnter 3 Keys")

        k1 = int(input("Key 1: "))
        k2 = int(input("Key 2: "))
        k3 = int(input("Key 3: "))

        if choice == "1":

            result = multilayer_encrypt(
                img,
                layer_choice,
                k1,
                k2,
                k3
            )

            out = path.rsplit(".", 1)[0] + "_multi_encrypted.png"

        else:

            result = multilayer_decrypt(
                img,
                layer_choice,
                k1,
                k2,
                k3
            )

            out = path.rsplit(".", 1)[0] + "_multi_decrypted.png"

        save_image(result, out)


# ==========================================================
# MAIN
# ==========================================================

def main():

    while True:

        banner()

        print("Encryption Mode:")
        print("1. Single Layer Encryption & Decryption")
        print("2. Multi Layer Encryption & Decryption")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            single_layer_menu()

        elif choice == "2":
            multi_layer_menu()

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
