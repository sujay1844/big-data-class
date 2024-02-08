#!/usr/bin/env python
import sys
import numpy as np


def read_centroids(file_path):
    centroids = []
    with open(file_path) as f:
        for line in f:
            centroid = np.array([float(x) for x in line.strip().split(',')])
            centroids.append(centroid)
    return centroids


def closest_centroid(point, centroids):
    distances = [np.linalg.norm(point - centroid) for centroid in centroids]
    return np.argmin(distances)


centroids = read_centroids("centroids.txt")

for line in sys.stdin:
    line = line.strip()

    point = np.array([float(x) for x in line.split(',')])

    centroid_idx = closest_centroid(point, centroids)

    print(f'{centroid_idx}\t{line}')
