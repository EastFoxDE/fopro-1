import numpy as np

class diffType:
    def __init__(self, value, derivative=0.0):
        self.value: float = value
        self.dvalue: float = derivative

    def __add__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        value = self.value + other.value
        derivative = self.dvalue + other.dvalue

        return diffType(value, derivative)

    def __radd__(self, other):
        return diffType(other, 0.0) + self

    def __sub__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)
        
        value = self.value - other.value
        derivative = self.dvalue - other.dvalue

        return diffType(value, derivative)

    def __rsub__(self, other):
        return diffType(other, 0.0) - self    

    def __mul__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        value = self.value * other.value
        derivative=self.dvalue * other.value + self.value * other.dvalue
 
        return diffType(value, derivative)

    def __rmul__(self, other):
        return diffType(other, 0.0) * self

    def __truediv__(self, other):
        if not isinstance(other, diffType):
           other = diffType(other, 0.0)

        value = self.value / other.value
        derivative = (self.dvalue * other.value - self.value * other.dvalue) / (other.value * other.value)

        return diffType(value, derivative)

    def __rtruediv__(self, other):
        return diffType(other, 0.0) / self

    def __pow__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        value = self.value ** other.value
        derivative = other.value * (self.value ** (other.value - 1.0))
        
        return diffType(value, derivative)

    def __rpow__(self, other):
        return diffType(other, 0.0) ** self

    def exp(self):
        value = np.exp(self.value)
        derivative = np.exp(self.value) * self.dvalue
        return diffType(value, derivative)
    
    def log(self):
        value = np.log(self.value)
        derivative = (1.0 / self.value) * self.dvalue
        return diffType(value, derivative)
    
    def sqrt(self):
        value = np.sqrt(self.value)
        derivative = 0.5 * (1.0 / np.sqrt(self.value)) * self.dvalue
        return diffType(value, derivative)
    
    def cos(self):
        value = np.cos(self.value)
        derivative = -np.sin(self.value) * self.dvalue
        return diffType(value, derivative)

    def sin(self):
        value = np.sin(self.value)
        derivative = np.cos(self.value)

        return diffType(value, derivative)   

    def show(self):
        print("Primal: ", self.value, "\tDerivative: ", self.dvalue, "(", self , ")")