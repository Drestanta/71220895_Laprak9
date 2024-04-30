numbers = []

while True:
    input_number = input("Masukkan angka (ketik 'done' untuk selesai): ")
    if input_number.lower() == 'done':
        break
    try:
        numbers.append(float(input_number))
    except ValueError:
        print("Masukan tidak valid.")

if numbers:
    print("Nilai maksimum:", max(numbers))
    print("Nilai minimum:", min(numbers))
else:
    print("Tidak ada angka yang dimasukkan.")
