from DataLoader import DataLoader

from Gene import Gene


class Adversary(object):
    def __init__(self):
        self.antigens = DataLoader().load_test_genes()

    def spawn(self) -> [Gene, str]:
        count = 0
        for antigen in self.antigens:
            if count % 10000 == 0:
                print("[%d/%d] antigens" % (count, len(self.antigens)))
            count += 1
            yield antigen
