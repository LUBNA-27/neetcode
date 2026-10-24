class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x=init
        for i in range (iterations):
            Derivative= 2*x
            x=x-learning_rate*Derivative
        return round(x,5)
