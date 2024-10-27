from sklearn import datasets
import pandas as pd

z = pd.read_csv('./csv/z_score.csv', header=0, index_col=0)

from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns

model = DBSCAN(eps=7, min_samples=5)
model_results = model.fit_predict(z)

predict = pd.DataFrame(model_results)
predict.index = z.index
predict.columns = ['predict']

pd.set_option('display.max_rows', None)

r = pd.concat([z, predict], axis=1)
print(r)

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)
tsne_results = tsne.fit_transform(z)

import seaborn as sns
from matplotlib import pyplot as plt

x = tsne_results[:, 0]
y = tsne_results[:, 1]

palette = sns.color_palette("bright", 10)
ax = sns.scatterplot(x=x, y=y, hue=model_results, legend='full', palette=palette)
for i, txt in enumerate(z.index):
    ax.text(x[i], y[i], txt)
plt.show()