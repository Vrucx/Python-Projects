import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Panjang password minimal 4 agar cukup aman.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    if length > 4:
        all_chars = lower + upper + digits + symbols
        password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Masukkan panjang password yang diinginkan: "))
        password = generate_password(length)
        print("Password yang dihasilkan:", password)
    except ValueError as e:
        print("Input tidak valid:", e)

if __name__ == "__main__":
    main()