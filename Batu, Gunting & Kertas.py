import random

def get_user_choice():
    choices = ['batu', 'gunting', 'kertas']
    while True:
        user_input = input("Pilih batu, gunting, atau kertas (atau ketik 'keluar' untuk berhenti): ").lower()
        if user_input == 'keluar':
            return None
        if user_input in choices:
            return user_input
        print("Pilihan tidak valid. Silakan coba lagi.")

def get_computer_choice():
    return random.choice(['batu', 'gunting', 'kertas'])

def determine_winner(user, computer):
    if user == computer:
        return 'seri'
    elif (user == 'batu' and computer == 'gunting') or \
         (user == 'gunting' and computer == 'kertas') or \
         (user == 'kertas' and computer == 'batu'):
        return 'menang'
    else:
        return 'kalah'

def main():
    print("Selamat datang di permainan Batu Gunting Kertas!")
    score_user = 0
    score_computer = 0
    round_number = 1

    while True:
        print(f"\n=== Ronde {round_number} ===")
        user_choice = get_user_choice()
        if user_choice is None:
            print("Terima kasih sudah bermain! Sampai jumpa!")
            break
        
        computer_choice = get_computer_choice()
        print(f"Komputer memilih: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == 'seri':
            print("Hasilnya seri!")
        elif result == 'menang':
            print("Kamu menang!")
            score_user += 1
        else:
            print("Kamu kalah!")
            score_computer += 1
        
        print(f"Skor: Kamu {score_user} - Komputer {score_computer}")
        round_number += 1

if __name__ == "__main__":
    main()