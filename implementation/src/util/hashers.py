"""
Methods for hashing values
"""
import numpy as np

def hash_n_to_1(x: np.ndarray, size: int) -> np.ndarray:
    """
    Given an `ndarray` `x` of shape `(n, ...)`,  return 
    an `ndarray` of shape `(...)` of pseudorandom integers 
    on the interval [0, `size`). Relatively anisotropic.
    """
    v = (x.cumsum(axis=0)) 
    v[0,...] += v[-1,...]
    v = v.prod(axis=0)
    v = (v * 7498924922429740871).view(int) % size
    return v