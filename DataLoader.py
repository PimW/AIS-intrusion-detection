import numpy as np

from Gene import Gene


class DataLoader(object):
    def __init__(self):
        self.self_genes_file = 'data-self-kpca-robust.csv'
        self.test_genes_File = 'data-intrusion-kpca-robust.csv'

    def load_genes(self) -> list:
        genes = []
        data = open(self.self_genes_file)
        for gene_array in data.readlines()[:10000]:
            gene_array = gene_array.strip().split(',')
            try:
                gene = Gene(np.array(gene_array, dtype='float32'))
            except Exception as e:
                print(gene_array)
                raise e
            genes.append(gene)
        return genes

    def load_test_genes(self):
        genes = []
        data = open(self.test_genes_File)
        data.readline()
        for gene_array in data.readlines()[:100000]:
            idx, *gene, label = gene_array.strip().split(',')
            gene = Gene(np.array(gene, dtype='float32'))
            genes.append((gene, label))
        return genes
