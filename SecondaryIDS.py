from Gene import Gene


class SecondaryIDS(object):
    def __init__(self):
        self.detectors = set()

        self.risk_factor = 0

    def add(self, anitbody: Gene):
        raise NotImplementedError()

    def detect(self, antigen: Gene) -> bool:
        for detector in self.detectors:
            if detector.match(antigen):
                return True
        return False

    def print_info(self, verbose=False):
        print("Secondary IDS: ")
        print("  %d detectors" % len(self.detectors))

        if verbose:
            for detector in self.detectors:
                print(detector)
