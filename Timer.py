import time

def timer(menit, detik):
    total_detik = menit * 60 + detik
    try:
        while total_detik >= 0:
            mins, secs = divmod(total_detik, 60)
            print(f"\rTimer: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
            total_detik -= 1
        print("\nWaktu habis!")
    except KeyboardInterrupt:
        print("\nTimer dibatalkan.")

def main():
    print("Timer Menit dan Detik")
    try:
        m = int(input("Masukkan menit: "))
        s = int(input("Masukkan detik: "))
        if m < 0 or s < 0 or s >= 60:
            print("Input tidak valid. Detik harus antara 0 dan 59, menit tidak boleh negatif.")
            return
        timer(m, s)
    except ValueError:
        print("Input harus berupa angka bulat.")

if __name__ == "__main__":
    main()