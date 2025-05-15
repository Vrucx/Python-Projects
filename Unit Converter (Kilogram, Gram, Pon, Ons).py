def convert_weight(value, from_unit, to_unit):
    unit_to_kg = {
        'kilogram': 1,
        'gram': 0.001,
        'pon': 0.453592,
        'ons': 0.0283495
    }

    if from_unit not in unit_to_kg or to_unit not in unit_to_kg:
        raise ValueError("Unit tidak valid. Gunakan kilogram, gram, pon, atau ons.")

    value_in_kg = value * unit_to_kg[from_unit]

    converted_value = value_in_kg / unit_to_kg[to_unit]
    return converted_value

def main():
    print("Selamat datang di Konverter Berat!")
    
    while True:
        try:
            value = float(input("Masukkan nilai berat yang ingin dikonversi: "))
            from_unit = input("Masukkan unit asal (kilogram, gram, pon, ons): ").lower()
            to_unit = input("Masukkan unit tujuan (kilogram, gram, pon, ons): ").lower()

            converted_value = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {converted_value} {to_unit}")

            another = input("Apakah Anda ingin mengonversi lagi? (ya/tidak): ").lower()
            if another != 'ya':
                print("Terima kasih telah menggunakan Konverter Berat!")
                break

        except ValueError as e:
            print(e)
        except Exception as e:
            print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    main()