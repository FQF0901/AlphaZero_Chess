import numpy as np

def compress_sparse_array(array, fill_value=0.):
    """
    Compress a 2D array into a sparse representation.
    
    Parameters:
        array (numpy.ndarray): The input 2D array.
        fill_value (float): The value to be considered as empty.
        
    Returns:
        numpy.ndarray: The compressed sparse array.
    """
    compressed = []
    compressed.append([array.shape[0], array.shape[1]])
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] != fill_value:
                compressed.append([i, j, array[i, j]])
    return np.array(compressed, dtype=object)

# Example usage:
array = np.array([[1, 0, 0],
                  [0, 2, 0],
                  [0, 0, 3]])
compressed_array = compress_sparse_array(array)
print(compressed_array)
