#!/usr/bin/env python
import sys
import numpy as np


def print_centroid(centroid_points):
    new_centroid = np.mean(centroid_points, axis=0)
    print(f"{new_centroid[0]:.3f},{new_centroid[1]:.3f}")


current_centroid = None
points = []

for line in sys.stdin:
    # Parse input from mapper
    centroid_idx, point_str = line.strip().split('\t')
    point = np.array([float(x) for x in point_str.split(',')])

    # If we're still on the same centroid
    if current_centroid == centroid_idx:
        points.append(point)
    else:
        if current_centroid is not None:
            print_centroid(points)

        current_centroid = centroid_idx
        points = [point]

if current_centroid is not None:
    print_centroid(points)
