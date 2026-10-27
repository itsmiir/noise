"""
Types of samplers that the interface supports.
"""
from typing import Callable, Tuple

import numpy as np

@export
def test(i: int) -> None:
    print(f"Hello {i} world!")


class NoiseSampler():
    """Base class for noise samplers."""
    def __init__(self, seed: int, name: str, salt: int) -> None:
        self.name = name
        self.seed: int = seed + salt
        self.rng = np.random.default_rng(self.seed)
        self.perm = np.arange(256, dtype=np.int64)
        self.perm = np.concatenate((self.perm, self.perm))
        self.rng.shuffle(self.perm)
        self.perm_11 = np.linspace(-1, 1, 256)
        self.rng.shuffle(self.perm_11)

    def sample_cuboid(self, x0: np.ndarray, x1: np.ndarray, count: tuple[int]) -> Tuple[np.ndarray, np.ndarray]:
        x = self.make_x(x0, x1, count)
        return self.sample(x)
    
    def sample(self, x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        return np.zeros(x.shape[1:]), np.zeros_like(x)
        
    def make_x(self, x0: np.ndarray, x1: np.ndarray, count: tuple[int]) -> np.ndarray:
        """
        Given n-dimensional start and end coordinates x0 and x1, create a hypercuboid of `prod(count)` points
        distributed between them, and return the coordinates of each point, coordinate-major.
        """
        grid = np.indices(count, dtype=float)
        reshape = (slice(None),) + (None,) * np.size(count)
        x = x0[reshape] + (x1 - x0)[reshape] * grid / np.subtract(count, 1)[reshape]
        return x
            