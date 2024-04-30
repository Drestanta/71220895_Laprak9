with open('file.txt', 'r') as file:
    lines = file.readlines()

print("====Isi Berita====")
open and print(file)

unique_words = []
print("====Kata Unik pada Berita====")
for line in lines:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print(unique_words)