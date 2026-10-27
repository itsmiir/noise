"""
Math helper functions.
"""
import numpy as np

def ternary(n: np.ndarray) -> np.ndarray:
    """Converts a integer in decimal to an array of ternary digits."""
    length = int(np.ceil(np.emath.logn(3, np.max(n)))) + 1
    out = np.zeros((length, *n.shape))
    for i in range(length):
        n, r = np.divmod(n, 3)
        out[i] = r
    return out.T.astype(int)