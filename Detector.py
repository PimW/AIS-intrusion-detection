import numpy as np

from Gene import Gene


class Detector(object):
    repulsion_value = 0.005

    def __init__(self, gene: Gene):
        self.gene = gene
        self.strength = 0.0
        self.tuning_value = 0.01
        self.threshold = 0.3

    def distance(self, other: Gene) -> float:
        return self.gene.distance(other)

    def match(self, other: Gene) -> bool:
        distance = self.distance(other)
        similarity = 1 / (1 + distance)
        return similarity > self.threshold

    def tune(self):
        self.threshold += self.tuning_value

    def repulse(self, other: Gene):
        direction = self.gene.array - other.array
        # direction = np.linalg.norm(direction)
        self.gene.array = self.gene.array + Detector.repulsion_value * direction

    def __str__(self):
        return "<threshold: %.2f, genes: %s>" % (self.threshold, self.gene)
