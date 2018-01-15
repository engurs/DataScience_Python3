import numpy as np

numpy_ndarray = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1])

another_numpy_ndarray = np.array([ 1.4,  1.5,  1.5,  1.3,  1.5,  1.3,  1.6,  1. ,  1.3,  1.4,  1. ,
        1.5,  1. ,  1.4,  1.3,  1.4,  1.5,  1. ,  1.5,  1.1,  1.8,  1.3,
        1.5,  1.2,  1.3,  1.4,  1.4,  1.7,  1.5,  1. ,  1.1,  1. ,  1.2,
        1.6,  1.5,  1.6,  1.5,  1.3,  1.3,  1.3,  1.2,  1.4,  1.2,  1. ,
        1.3,  1.2,  1.3,  1.3,  1.1,  1.3])

# Computing the variance

# Array of differences to mean
differences = numpy_ndarray - np.mean(numpy_ndarray)

# Square the differences
diff_sq = differences ** 2

# Compute the mean square difference
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy
variance_np = np.var(numpy_ndarray)
print(variance_explicit, variance_np)


# Compute the standard deviation and the variance

variance = np.var(numpy_ndarray)

# Print the square root of the variance
print(variance ** 0.5)

# Print the standard deviation
print(np.std(numpy_ndarray))  # Should be same


# Covariance matrix
# Imagine arrays are width and length of same type objects

covariance_matrix = np.cov(numpy_ndarray,another_numpy_ndarray)
print(covariance_matrix)  # Look at symmetry, entry [1,0] is the same as entry [0,1]

# Extract covariance of length and width of objects:
object_cov = covariance_matrix[0, 1]
# Print the length/width covariance
print(object_cov)

# Pearson correlation coefficient
# is often easier to interpret than the covariance


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0, 1]


# Compute Pearson correlation coefficient
r = pearson_r(numpy_ndarray, another_numpy_ndarray)
print(r)


