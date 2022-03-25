import word_database as wd

s = []


def search(word):
    all = False
    good_part = False
    bad_part = False

    if s in wd.database:
        s.append(word)
        all = True
        return s, all, good_part, bad_part


    w = ''
    for ch in word:
        if not wd.is_vowel(ch):
            w += ch

    if len(s) == 0:
        for key, value in wd.datadict.items():
            if len(w) in range(len(value) - 1, len(value) + 1):
                if w in value or value in w:
                    s.append(key)
                    good_part = True

    if len(s) == 0:
        for key, value in wd.datadict.items():
            if len(w) in range(len(value) - 2, len(value) + 3):
                if w in value or value in w:
                    s.append(key)
                    bad_part = True

    return s, all, good_part, bad_part



word = input('Write the word you wnat to search: -> ')
word = word.lower()

result = search(word)

output = result[0]
all = result[1]
good_part = result[2]
bad_part = result[3]



if all and not good_part and not bad_part:
    print("Congratulation! There is the word you searched -> ", word)
elif not all and good_part and not bad_part:
    print("There is no the word you searched, but there are other words that are very similar to your word -> ", output)
elif not all and not good_part and bad_part:
    print("There is no the word you searched, but there are other words that are a little similar to your word -> ", output)
else:
    print("Sorry, your word is extraordinary and has no friends in my database. Bye )")
