import pandas
from matplotlib import pyplot
from sklearn.cluster import KMeans

score = pandas.read_csv('score2.csv', encoding='utf_8')
model = KMeans(n_clusters=3).fit(
    score[['English', 'Japanese']])
print(model.labels_)
