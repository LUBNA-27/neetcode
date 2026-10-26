import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        new_z=z-max(z)
        return np.round((np.exp(new_z)/np.sum(np.exp(new_z))),4)
        
