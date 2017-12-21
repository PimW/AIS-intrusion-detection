from PrimaryIDS import PrimaryIDS
from SecondaryIDS import SecondaryIDS

CONFIG = {
    'secondary_ids_count': 10
}


print("Creating primary IDS")
ids = PrimaryIDS()

ids.print_info(verbose=True)

ids.run()
