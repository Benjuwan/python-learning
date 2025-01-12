number = input('Number:')
if number == '123456':
    print('1st Prize:Money')
elif number[-4:] == '7890':
    print('2nd Prize:Gift Box')
elif number[-2:] == '05':
    print('3nd Prize:Stamp Sheet')
else:
    print('Lose')
