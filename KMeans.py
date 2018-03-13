import numpy as np

X = np.array([[1,2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = 0.001
        self.max_iter = max_iter

    def fit(self, data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        # Iteration with in max_iter, but we still have break out procedure
        # as long as we reach optimized centroid. Of course, every iteration
        # we need to empty the classification

        for _ in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            # Calculate the distacne and choose the classification
            for each in data:
                distances = [np.linalg.norm(each - self.centroids[centroid])
                             for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(each)

            # Update the centroids, but remember to save the previous one
            # for comparasion purpose

            prev_centroids = dict(self.centroids)

            for i in self.centroids:
                self.centroids[i] = np.mean(self.classifications[i], axis=0)

            # Check whether it's optimized within the tolerance, we need to
            # check both of the clusters

            optimized = True

            for i in self.centroids:
                orig_centroid = prev_centroids[i]
                curr_centroid = self.centroids[i]
                if np.sum((curr_centroid - orig_centroid) / orig_centroid
                          *100) > self.tol:
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        classifications = {}

        for i in range(self.k):
            classifications[i] = []

        for each in data:
                distances = [np.linalg.norm(each - self.centroids[centroid])
                             for centroid in self.centroids]
                classification = distances.index(min(distances))
                classifications[classification].append(each)

        return classifications

