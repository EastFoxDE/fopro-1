import numpy as np

class diffType:
    def __init__(self, value, derivative=0.0):
        self.value: float = value
        self.dvalue: float = derivative

    def __add__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        return diffType(self.value + other.value, self.dvalue + other.dvalue)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)
        
        return diffType(self.value - other.value, self.dvalue - other.dvalue)

    def __rsub__(self, other):
        return diffType(other, 0.0) - self    

    def __mul__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        return diffType(
            self.value * other.value,
            self.dvalue * other.value + self.value * other.dvalue
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, diffType):
            other = diffType(other, 0.0)

        return diffType(
            self.value / other.value,
            (self.dvalue * other.value - self.value * other.dvalue) / (other.value ** 2)
        )

    def __rtruediv__(self, other):
        return diffType(other, 0.0) / self

    def __pow__(self, other):
        if isinstance(other, diffType):
            value = self.value ** other.value
            derivative = value * (
                other.dvalue * np.log(self.value) +
                (other.value * self.dvalue / self.value)
            )
            return diffType(value, derivative)
        else:
            return diffType(self.value ** other, other * (self.value ** (other - 1)) * self.dvalue)

    def __rpow__(self, other):
        return diffType(other, 0.0) ** self

    def exp(self):
        value = np.exp(self.value)
        return diffType(value, value * self.dvalue)
    
    def log(self):
        return diffType(np.log(self.value), (1.0 / self.value) * self.dvalue)
    
    def sqrt(self):
        return diffType(np.sqrt(self.value), 0.5 * self.dvalue / np.sqrt(self.value))
    
    def cos(self):
        return diffType(np.cos(self.value), -np.sin(self.value) * self.dvalue)

    def sin(self):
        return diffType(np.sin(self.value), np.cos(self.value) * self.dvalue)

    def __repr__(self):
        return f"diffType(value={self.value}, derivative={self.dvalue})"

    def show(self):
        print(f"Primal: {self.value}, Derivative: {self.dvalue}")

