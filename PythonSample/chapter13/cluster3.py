import pandas
from matplotlib import pyplot
from sklearn.cluster import KMeans

score = pandas.read_csv('score2.csv', encoding='utf_8')
model = KMeans(n_clusters=3).fit(
    score[['English', 'Japanese']])

score['Cluster'] = model.labels_
score.plot.scatter('English', 'Japanese', 
                   s=100, c=score['Cluster'], 
                   edgecolor='black', figsize=(6, 6))
pyplot.savefig('scatter2.png')
pyplot.show()
