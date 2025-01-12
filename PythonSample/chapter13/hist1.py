import pandas
from matplotlib import pyplot

score = pandas.read_csv('score2.csv', encoding='utf_8')
pyplot.figure('Math')
pyplot.xlabel('Score')
pyplot.ylabel('Count')
pyplot.hist(score['Math'])
pyplot.savefig('hist1.png')
pyplot.show()
