import random

from DataLoader import DataLoader
from SecondaryIDS import SecondaryIDS
from DetectorGenerator import DetectorGenerator

from Adversary import Adversary
from Gene import Gene


class PrimaryIDS(object):
    def __init__(self):
        print("Initializing IDS..")
        self.affinity_threshold = 0.3
        self.alert_threshold = 1
        self.secondaryIDS_count = 1
        self.detector_set_size = 50

        self.secondaryIDSs = []

        print("Loading self..")
        self.self = DataLoader().load_genes()

        self.detector_generator = DetectorGenerator()
        self.detector_generator.test_set = self.self

        print("Generating detector agents..")
        self.create_secondary_ids()

        print("Creating adversary..")
        self.adversary = Adversary()

        # Stats
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0

    def create_secondary_ids(self):
        for i in range(self.secondaryIDS_count):
            print("Creating detector set [%d/%d].." % (i + 1, self.secondaryIDS_count))
            secondary_ids = SecondaryIDS()
            secondary_ids.detectors = self.generate_detector_set()
            self.add_secondary_ids(secondary_ids)

    def add_secondary_ids(self, secondary_ids: SecondaryIDS):
        self.secondaryIDSs.append(secondary_ids)

    def generate_detector_set(self):
        return self.detector_generator.generate_detector_set(self.detector_set_size)

    def detect(self, antigen: Gene):
        votes = 0

        for secondary_ids in self.secondaryIDSs:
            if secondary_ids.detect(antigen):
                votes += 1
        if votes >= self.alert_threshold:
            return True
        return False

    def run(self):
        print("Running detection..")
        for (antigen, label) in self.adversary.spawn():
            result = self.detect(antigen)
            if result and label != 'normal':
                self.tp += 1
            elif result and label == 'normal':
                self.fp += 1
            elif not result and label != 'normal':
                self.fn += 1
            elif not result and label == 'normal':
                self.tn += 1
            else:
                print(result)
                print(label)
                print(antigen)
                raise Exception("Unexpected values")

        self.print_stats()

    def print_stats(self):
        detection_rate = round(self.tp / (self.tp + self.fn) * 100)
        false_alarm_rate = round(self.fp / (self.tn + self.fp) * 100)

        print("Stats: ")
        print("True Positive: %d" % self.tp)
        print("False Positive: %d" % self.fp)
        print("True Negative: %d" % self.tn)
        print("False Negative: %d" % self.fn)
        print("Detection rate %d%%. False alarm rate %d%%" % (detection_rate, false_alarm_rate))

    def print_info(self, verbose=False):
        print("Primary IDS: ")

        if verbose:
            for secondary_ids in self.secondaryIDSs:
                secondary_ids.print_info(verbose)
