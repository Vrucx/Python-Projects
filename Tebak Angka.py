import random

def main():
    print("Selamat datang di game Tebak Angka!")
    play_again = 'ya'

    while play_again.lower() == 'ya':
        angka_rahasia = random.randint(1, 100)
        tebakan = None
        percobaan = 0

        print("Saya sudah memilih sebuah angka antara 1 sampai 100. Coba tebak ya!")

        while tebakan != angka_rahasia:
            try:
                tebakan = int(input("Masukkan tebakanmu: "))
                percobaan += 1

                if tebakan < angka_rahasia:
                    print("Terlalu kecil, coba lagi.")
                elif tebakan > angka_rahasia:
                    print("Terlalu besar, coba lagi.")
                else:
                    print(f"Selamat! Kamu menebak benar dalam {percobaan} kali percobaan.")
            except ValueError:
                print("Input tidak valid. Masukkan angka bulat.")

        play_again = input("Mau main lagi? (ya/tidak): ")

    print("Terima kasih sudah bermain! Sampai jumpa.")

if __name__ == "__main__":
    main()