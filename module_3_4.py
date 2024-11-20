def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        a = root_word.lower()
        b = words.lower()
        i = words.count(a)
        if i > 0:
            d = ''.join(words)
            same_words.append(d)
    for s in range(len(other_words)):
        a = root_word.lower()
        f = other_words[s].lower()
        if f in a != 0:
            same_words.append(other_words[s])
    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')