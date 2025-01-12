with open('message.txt', encoding='utf-8') as file:
    for count, text in enumerate(file, 1):
        print(count, text, end='')
