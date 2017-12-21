import numpy as np

from Gene import Gene


class Detector(object):
    def __init__(self, gene: Gene):
        self.gene = gene
        self.strength = 0.0
        self.tuning_value = 0.05
        self.threshold = 0.3

    def distance(self, other: Gene) -> float:
        return self.gene.distance(other)

    def match(self, other: Gene) -> bool:
        distance = self.distance(other)
        return (2 - distance) / 2 > self.threshold

    def tune(self):
        self.threshold += self.tuning_value

    def __str__(self):
        return "<threshold: %.2f, genes: %s>" % (self.threshold, self.gene)