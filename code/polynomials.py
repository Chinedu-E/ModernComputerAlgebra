import numpy as np
from sympy import Symbol, Function


class Polynomial:

    def __init__(self,
                 args: list[int | float] | np.ndarray):
        self.coeffs = np.array(args)
        self.string = self.generate_string()

    def __str__(self):
        poly_string = self.generate_string()
        self.string = poly_string
        return poly_string

    def generate_string(self):
        poly_string = ""
        x = Symbol("x")
        for i in range(len(self)):
            poly_string += str((x ** i) * self.coeffs[i])
            if i != len(self) - 1:
                poly_string += " + "
        return poly_string

    def __add__(self, other):
        if isinstance(other, Polynomial):
            k = max(len(other), len(self))
            ph1 = np.zeros(shape=k)
            ph2 = np.zeros(shape=k)
            ph1[:len(self)] = self.coeffs
            ph2[:len(other)] = other.coeffs
            new_poly = ph1 + ph2
            return Polynomial(new_poly)

        elif isinstance(other, int) or isinstance(other, float):
            ph = other + self.coeffs
            return Polynomial(ph)

        else:
            return NotImplementedError

    def __mul__(self, other):
        ...

    def __truediv__(self, other):
        ...

    def __call__(self, inp: int | float) -> int | float:
        x = Symbol("x")
        f1 = Function("poly")(self.string)
        f1 = f1.subs(x, inp)
        return f1.args[0]

    def __len__(self):
        return len(self.coeffs)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return np.array_equal(self.coeffs, other.coeffs)
        return NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            k = max(len(other), len(self))
            ph1 = np.zeros(shape=k)
            ph2 = np.zeros(shape=k)
            ph1[:len(self)] = self.coeffs
            ph2[:len(other)] = other.coeffs
            new_poly = ph1 - ph2
            return Polynomial(new_poly)

        elif isinstance(other, int) or isinstance(other, float):
            ph = self.coeffs - other
            return Polynomial(ph)

        else:
            return NotImplementedError
