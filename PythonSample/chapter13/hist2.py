import pandas
from matplotlib import pyplot

score = pandas.read_csv('score2.csv', encoding='utf_8')
score.hist()
pyplot.savefig('hist2.png')
pyplot.show()
