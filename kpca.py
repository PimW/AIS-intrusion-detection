from sklearn.preprocessing import KernelCenterer
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np


def KernelPCA(X):
    # pdist to calculate the squared Euclidean distances for every pair of points
    # in the 100x2 dimensional dataset.

    sq_dists = pdist(X, 'sqeuclidean')

    # Variance of the Euclidean distance between all pairs of data points.
    variance = np.var(sq_dists)

    # squareform to converts the pairwise distances into a symmetric 100x100 matrix
    mat_sq_dists = squareform(sq_dists)

    # set the gamma parameter equal to the one I used in scikit-learn KernelPCA
    gamma = 15

    # Compute the 100x100 kernel matrix
    K = exp(-gamma * mat_sq_dists)

    # Center the kernel matrix
    kern_cent = KernelCenterer()
    K = kern_cent.fit_transform(K)

    # Get eigenvalues in ascending order with corresponding
    # eigenvectors from the symmetric matrix
    eigvals, eigvecs = eigh(K)

    # Get the eigenvectors that corresponds to the highest eigenvalue
    X_pc1 = eigvecs[:, -1]
    return X_pc1