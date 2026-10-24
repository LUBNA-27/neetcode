import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        out=[]
        for i in z:
            sigmoid= 1/(1+np.exp(-i))
            out.append(sigmoid)
        return np.round(np.array(out),5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        out=[]
        for j in z:
            if j>0:
                out.append(j)
                continue
            else:
                out.append(0.0)
        return np.round (np.array(out),5)
