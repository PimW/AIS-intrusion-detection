import numpy as np
from scipy.spatial.distance import euclidean


class Gene(object):
    distance_measure = ''
    lifespan = 100
    size = 5

    def __init__(self, gene_array):
        self.activation = 0
        self.array = gene_array

    def match_many(self):
        raise NotImplementedError()

    def match(self, other) -> bool:
        raise NotImplementedError()

    def distance(self, other) -> float:
        return euclidean(self.array, other.array)

    def __str__(self):
        return str(self.array)
