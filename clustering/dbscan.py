import sys
import ast
import argparse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE

def search_range(s):
    v = ast.literal_eval(s)
    if type(v) is not tuple:
        raise argparse.ArgumentTypeError(f'argument {v} is not a tuple')

    for x in v:
        if type(x) is not float and type(x) is not int:
            raise argparse.ArgumentTypeError(f'element {x} in argument {v} is not numeric')
    
    return v

def dbscan(csv_path, eps, minpts):
    df = pd.read_csv(csv_path, header=0, index_col=0)

    if minpts == 0:
        minpts = round(np.log(len(df)))

    print(f'default minpts: {minpts}')

    model = DBSCAN(eps=eps, min_samples=minpts)
    model_results = model.fit_predict(df)

    # 결과 저장
    predict = pd.DataFrame(model_results)
    predict.index = df.index
    predict.columns = ['predict']
    predict.to_csv('./csv/dbscan_predict.csv')

    # 시각화
    tsne = TSNE(n_components=2)
    tsne_results = tsne.fit_transform(df)

    x = tsne_results[:, 0]
    y = tsne_results[:, 1]

    palette = sns.color_palette("bright", 10)
    ax = sns.scatterplot(x=x, y=y, hue=model_results, legend='full', palette=palette)
    for i, txt in enumerate(df.index):
        ax.text(x[i], y[i], txt)
    plt.show()

def grid_search(csv_path, eps_range, mpts_range):
    pd.set_option('display.max_rows', None)

    df = pd.read_csv(csv_path, header=0, index_col=0)

    eps_list = []
    minpts_list = []
    result_list = []

    for eps in np.arange(eps_range[0], eps_range[1], eps_range[2]):
        for minpts in np.arange(mpts_range[0], mpts_range[1], mpts_range[2]):
            model = DBSCAN(eps=eps, min_samples=minpts)
            model_results = model.fit_predict(df)

            eps_list.append(eps)
            minpts_list.append(minpts)
            result_list.append([np.count_nonzero(model_results == -1), np.max(model_results)])

    grid = pd.DataFrame(result_list, index=[eps_list, minpts_list], columns=['outliers', 'clusters'])
    grid.index.names = ['eps', 'minpts']

    print(grid)

def show_kdist(csv_path):
    df = pd.read_csv(csv_path, header=0, index_col=0)

    k = 4
    nn = NearestNeighbors(n_neighbors=k)
    neighbors = nn.fit(df)
    distances, _ = neighbors.kneighbors(df)

    distances = np.sort(distances[:, k-1])

    plt.plot(distances)
    plt.xlabel('sorted k-distances')
    plt.ylabel('k-distance value')
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="",
        help="path of csv file",
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        default=0,
        help="mode type (0: dbscan clustering, 1. grid search, 2: show k-distance graph)",
    )
    parser.add_argument(
        "-e",
        "--epsilon",
        type=float,
        default=0,
        help="epsilon value for dbscan clustering",
    )
    parser.add_argument(
        "-n",
        "--minpts",
        type=int,
        default=0,
        help="min points for dbscan clustering",
    )
    parser.add_argument(
        "-r",
        "--epsilon-range",
        type=search_range,
        default=(),
        help="epsilon range for grid test",
    )
    parser.add_argument(
        "-s",
        "--minpts-range",
        type=search_range,
        default=(),
        help="minpts range for grid test",
    )
    args = parser.parse_args()
    assert args.path != ""

    if args.mode == 0:
        sys.exit(dbscan(args.path, args.epsilon, args.minpts))
    elif args.mode == 1:
        grid_search(grid_search(args.path, args.epsilon_range, args.minpts_range))
    elif args.mode == 2:
        sys.exit(show_kdist(args.path))