import sys
import argparse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import os
os.environ["OMP_NUM_THREADS"] = "1"

def data_load(csv_path):
    data_frame = pd.read_csv(csv_path)

    X = data_frame.iloc[:, 1:].values

    champion_names = data_frame.iloc[:, 0].values
    champion_names = champion_names.tolist()

    column_list = data_frame.iloc[:, 1:].columns.values
    column_list = column_list.tolist()

    return X, champion_names, column_list

def k_means(csv_path, k):
    X, champion_names, column_list = data_load(csv_path)

    kmeans = KMeans(n_clusters=k, n_init = 30, tol=0.00003, max_iter = 5000, random_state=0)
    kmeans.fit(X)
    labels = kmeans.labels_
    
    # 클러스터 레이블 저장 (CSV 형식)
    labeling_df = pd.DataFrame({
        'champion_name': champion_names,
        'cluster_Label': labels.tolist()
    })
    save_path_label = f'kmeans_labels_k={k}.csv'
    labeling_df.to_csv(save_path_label, index=False)
    
    # 클러스터 중심점 저장 (CSV 형식)
    centroids = kmeans.cluster_centers_
    save_path_centroids = f'kmeans_centroids_k={k}.csv'
    pd.DataFrame(centroids, columns=column_list).to_csv(save_path_centroids, index=False)

    # PCA로 차원 축소 (138차원 -> 2차원) ; 그래프로 시각화 하기 위해
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    # 시각화
    plt.figure(figsize=(18, 9))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, s=50, alpha=0.7, cmap='viridis')
    
    # 각 데이터 포인트에 챔피언 이름 추가
    for i, name in enumerate(champion_names):
        plt.annotate(name, (X_pca[i, 0], X_pca[i, 1]), textcoords="offset points", xytext=(7, 7), ha='center')
    
    # 클러스터 중심 표시
    centers_pca = pca.transform(kmeans.cluster_centers_)
    plt.scatter(centers_pca[:, 0], centers_pca[:, 1], c='red', s=300, alpha=0.75, marker='X')
    
    plt.title('K-Means Clustering')
    plt.show()

def show_sse(csv_path):
    X, _, _ = data_load(csv_path)

    sse_list = []
    for k in range(5, 20):
        kmeans = KMeans(n_clusters=k, n_init = 30, tol=0.00003, max_iter = 5000, random_state=0)
        kmeans.fit(X)
        sse_list.append(kmeans.inertia_)
    # SSE 그래프 그리기
    plt.plot(range(5, 20), sse_list, marker='o')
    plt.xlabel('number of clustering')
    plt.ylabel('SSE')
    plt.show()

def show_silhouette(csv_path):
    X, _, _ = data_load(csv_path)

    silhouette_score_list = []
    for k in range(5, 20):
        kmeans = KMeans(n_clusters=k, n_init = 30, tol=0.00003, max_iter = 5000, random_state=0)
        kmeans.fit(X)
        score = silhouette_score(X, kmeans.labels_)
        silhouette_score_list.append(score)
    plt.plot(range(5, 20), silhouette_score_list, marker='o')
    plt.xlabel('number of clustering')
    plt.ylabel('silhouette score')
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
        help="mode type (0: k-means clustering, 1: show sse, 2 : show silhouette scores)",
    )
    parser.add_argument(
        "-k",
        "--k_num",
        type=int,
        default=9,
        help="number of clustering",
    )
    args = parser.parse_args()

    assert args.path != ""

    if args.mode == 0:
        sys.exit(k_means(args.path, args.k_num))
    elif args.mode == 1:
        sys.exit(show_sse(args.path))
    elif args.mode == 2:
        sys.exit(show_silhouette(args.path))