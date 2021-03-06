import random

from Gene import Gene
from Detector import Detector


class DetectorGenerator(object):
    def __init__(self):
        self.test_set = []
        self.weak_detector_set = set()

        self.binding_treshold = 0.0
        self.power_treshold = 0.9

    def create_detector(self) -> Detector:
        gene_array = []
        for i in range(Gene.size):
            gene_array.append(random.random())
        gene = Gene(gene_array)
        return Detector(gene)

    def generate(self) -> Detector:
        detector = self.create_detector()

        detector_power = 0

        for self_gene in self.test_set:
            while detector.match(self_gene):
                self.weak_detector_set.add(detector)
                detector_power -= 1
                detector.tune()
                detector.repulse(self_gene)
            else:
                detector_power += 1

        if (detector_power / len(self.test_set)) > self.power_treshold:
            return detector
        else:
            raise Exception("Rejected with power %f" % (detector_power / len(self.test_set)))

    def generate_detector_set(self, ds_size=100) -> set:
        detector_set = set()
        count = 0
        while len(detector_set) < ds_size:
            print("Gene [%d/%d]" % (count + 1, ds_size))
            gene = self.generate()
            if gene:
                detector_set.add(gene)
            count += 1
        return detector_set
