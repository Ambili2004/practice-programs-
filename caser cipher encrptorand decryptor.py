# ─── Caesar Cipher ───────────────────────────────────────────

def encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(text):
    print("\nBrute Force — all possible shifts:\n")
    for shift in range(1, 26):
        print(f"  Shift {shift:>2}: {encrypt(text, shift)}")


# ─── Main Program ─────────────────────────────────────────────

def main():
    print("=== Caesar Cipher ===\n")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force\n")

    # Loop until a valid choice is entered
    while True:
        choice = input("Choose (1/2/3): ").strip()
        if choice in ("1", "2", "3"):
            break
        print(" Invalid choice! Please enter 1, 2, or 3.\n")

    if choice in ("1", "2"):
        text = input("Enter text  : ")

        #  Loop until a valid shift number is entered
        while True:
            try:
                shift = int(input("Enter shift (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print(" Shift must be between 1 and 25.\n")
            except ValueError:
                print(" Please enter a number, not letters.\n")

        if choice == "1":
            print(f"\n Encrypted : {encrypt(text, shift)}")
        else:
            print(f"\n Decrypted : {decrypt(text, shift)}")

    elif choice == "3":
        text = input("Enter ciphertext: ")
        brute_force(text)


if __name__ == "__main__":
    main()