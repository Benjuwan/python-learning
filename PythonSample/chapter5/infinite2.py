while True:
    word = input('word: ')
    if not word:
        break
    print(len(set(word)))
    print(set(word))
