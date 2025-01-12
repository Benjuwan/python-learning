number = input('Number:')
print('1st Prize:Money' if number == '123456' else
      '2nd Prize:Gift Box' if number[-4:] == '7890' else
      '3nd Prize:Stamp Sheet' if number[-2:] == '05' else 'Lose')
