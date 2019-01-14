from PrimaryIDS import PrimaryIDS
from SecondaryIDS import SecondaryIDS
from Detector import Detector
import time


CONFIG = {
    'secondary_ids_count': 10
}


# print("Creating primary IDS")
# ids = PrimaryIDS()
#
# ids.print_info(verbose=True)
#
#
# start = time.time()
#
# print(time.time()-start)


def test():
    for repulsion_value in (0.005, 0.01, 0.02, 0.05):
        print("Testing with repulsion value %f" % repulsion_value)
        f = open('detector-repulsion-%f-stats.txt' % repulsion_value,'w')
        f.write('tp,tn,fp,fn\n')
        for i in range(20):
            print("Run [%d/20]" % (i + 1))
            Detector.repulsion_value = repulsion_value
            ids = PrimaryIDS()

            ids.run()
            f.write('%d,%d,%d,%d\n' % (ids.tp, ids.tn, ids.fp, ids.fn))
        f.close()

test()