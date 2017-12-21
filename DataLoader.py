import numpy as np

from Gene import Gene


class DataLoader(object):
    def __init__(self):
        self.self_genes_file = 'data-self-kpca-robust.csv'
        self.test_genes_File = 'data-intrusion-kpca-robust.csv'

    def load_genes(self) -> list:
        genes = []
        data = open(self.self_genes_file)
        for gene_array in data.readlines():
            gene_array = gene_array.strip().split(',')
            try:
                gene = Gene(np.array(gene_array, dtype='float32'))
            except:
                print(gene_array)
                raise
            genes.append(gene)
        return genes

    def load_test_genes(self):
        genes = []
        data = open(self.test_genes_File)  # np.loadtxt(self.self_genes_file, delimiter=',')
        data.readline()
        for gene_array in data.readlines():
            idx, *gene, label = gene_array.strip().split(',')
            gene = Gene(np.array(gene, dtype='float32'))
            genes.append((gene, label))
        return genes