def append_indices(indices):
    extented_indices = indices
    for index in indices:
        extented_indices.append(index)
    print(extended_indices)
    return extended_indices

def make_alph_range(indices): #or index if it's the latter case
    if type(indices) is list:
        return [index - (index // 26) * 26 if index >= 26 else index for index in indices]
    elif type(indices) is int:
        index = indices
        if index >= 26:
            return index - (index // 26) * 26
        else: return index
    #also the idea I'm too lazy to implement
    #because I'm travelling and feeling sick in the stomach
    #the function argument is called 'x' for simplicity
    #now the code
    #indices = []
    #indices.append(x)
    #return return [index - (index // 26) * 26 if index >= 26 else index for index in indices]

def shift(word, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    key_indices = [alph.index(char) for char in key]
    word_indices = [alph.index(char) for char in word]
    multipler = len(word) // len(key) + 1
    while multipler > 0:
        append_indices(key_indices)
        multipler -= 1

    crypto = []
    for word_index in word_indices:
        for key_index in key_indices:
            print(make_alph_range(key_index + word_index), crypto)
            crypto.append(alph[make_alph_range(key_index + word_index)])
            break
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
