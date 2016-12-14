def append_indices(indices):
    ext_indices = indices
    step = 0
    stop = len(indices)
    extended_indices = indices
    while step < stop:
        extended_indices.append(indices[step])
        step += 1
    return extended_indices

def make_alph_range(indices): #or index if it's the latter case
    if type(indices) is list:
        return [index - (index // 26) * 26 if index >= 26 else index for index in indices]
    elif type(indices) is int:
        index = indices
        if index >= 26:
            return index - (index // 26) * 26
        else: return index


def shift(word, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    key_indices = [alph.index(char) for char in key]
    word_indices = [alph.index(char) for char in word]
    multipler = len(word) // len(key) + 1
    while multipler > 0:
        append_indices(key_indices)
        multipler -= 1

    crypto = []
    key_index = 0
    for word_index in word_indices:
         crypto.append(alph[make_alph_range(key_indices[key_index] + word_index + 1)])
         key_index += 1
    print(crypto)
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

print("""Polialabetik Sifreleme:
Lutfen bir kelime ve bir anahtar kelime saglayiniz.\n""")

key = get_word("Anahtar Kelime: ")

results = []
go_on = True
while go_on is True:
    word = get_word("Kelime: ")
    results.append(shift(word, key))
    while True:
        try:
            go_on = bool(int(input("Devam etmek icin herhangi bir sayiya,\nDurmak icin 0a basiniz: ")))
            break
        except ValueError:
            print("Lutfen sadece sayi giriniz!")

for end_word in results:
    print(end=" ")
    for char in end_word:
        print(char,end="")
