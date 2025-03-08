def generate_code_map():
    code_map = {}
    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_chars = digits + letters
    for i, char in enumerate(all_chars):
        code_map[char] = f"{i:07d}"
    return code_map


def generate_reverse_code_map(code_map):
    reverse_code_map = {v: k for k, v in code_map.items()}
    return reverse_code_map


def decrypt_message(encrypted_message, reverse_code_map):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 7):
        code = encrypted_message[i:i + 7]
        if code in reverse_code_map:
            decrypted_message += reverse_code_map[code]
    return decrypted_message


def main():
    code_map = generate_code_map()
    reverse_code_map = generate_reverse_code_map(code_map)

    encrypted_message = input("Enter the encrypted message: ")
    decrypted_message = decrypt_message(encrypted_message, reverse_code_map)

    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
