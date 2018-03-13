import numpy as np


X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11],
              [8,2],
              [10,2],
              [9,3],])

class MeanShift:
    def __init__(self, radius=4):
        self.radius = radius

    def fit(self, data):
        centroids = {}

        # Initial number of centroids is the same as
        # the length of the dataset
        for i in range(len(data)):
            centroids[i] = data[i]

        while True:
            new_centroids = []

            for i in centroids:
                centroid = centroids[i]
                in_bandwidth = []

                # Clustering one by one
                for each in data:
                    if np.linalg.norm(each-centroid) < self.radius:
                        in_bandwidth.append(each)

                # Update the centroid
                new_centroid = np.mean(in_bandwidth, 0)

                # Save the centroid into list, here it's important, because np.ndarray
                # can not be sorted, so we have to use tuple version.
                new_centroids.append(tuple(new_centroid))

            uniques = sorted(list(set(new_centroids)))

            # Save previous centroids for comparsion purpose
            prev_centroids = dict(centroids)

            optimized = True

            # Update centroids for next loop
            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            for i in centroids:
                if not np.array_equal(prev_centroids[i], centroids[i]):
                    optimized = False

                if not optimized:
                    break

            if optimized:
                break

        self.centroids = centroids

            
