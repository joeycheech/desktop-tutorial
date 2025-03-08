def generate_code_map():
    code_map = {}
    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_chars = digits + letters
    for i, char in enumerate(all_chars):
        code_map[char] = f"{i:07d}"
    return code_map

def encrypt_message(message, code_map):
    encrypted_message = ""
    for char in message:
        if char in code_map:
            encrypted_message += code_map[char]
        else:
            continue
    return encrypted_message

def main():
    code_map = generate_code_map()
    message = input("Enter your message: ")
    encrypted_message = encrypt_message(message, code_map)
    print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
