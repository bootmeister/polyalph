def make_alph_range(indices):
    return [index - (index // 26) * 26 if index >= 26 else index for index in indices]

def shift(word, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    key_indices = [alph.index(char) for char in key]
    word_indices = [alph.index(char) for char in word]
    word_indices = make_alph_range(word_indices)
    key_indices = make_alph_range(key_indices)
    crypto = "".join([alph[index] for index in indices])
    return crypto


def get_word(ask):
    word = "123"
    while not isalpha(word):
        word = input(ask)
        if isalpha(word) == False:
            print("Lutfen kelimenizde sayi ya da ozel karakter kullanmayiniz!")
    return word.lower()


def isalpha(word):
    has_num = False
    for char in word:
        try:
            char = int(char)
            has_num = True
        except ValueError:
            pass
    return not has_num

print("""Sezar sifrelmesi:
Lutfen bir kelime ve bir kaydirma sayisi saglayiniz.\n""")

key = get_word("Anahtar: ")

result = []
go_on = True
while go_on is True:
    word = get_word("Kelime: ")
    result.append(shift(word, key))
    while True:
        try:
            go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
            break
        except ValueError:
            print("Lutfen sadece sayi giriniz!")
print(" ".join(result))
