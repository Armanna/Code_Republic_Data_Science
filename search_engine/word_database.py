from faker import Faker

def is_vowel(ch):
    if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False

fake = Faker()

database = []
datadict = {}

for i in range(100000):
    word = fake.word()
    database.append(word)

    w = ''
    for ch in word:
        if not is_vowel(ch):
            w += ch
    datadict[word] = w


# print(datadict)






