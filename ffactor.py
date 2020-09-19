#Using Newton Raphson method to find the friction factor
from math import log10
import sys

PRECISION = 0.00001
INITIAL_GUESS = 0.01


class Data():
    """
    A Class to represent a f,Re and ed data.
    """
    def __init__(self):
        self.Re = 0
        self.ed = 0
        self.f ='0'

    def read_ed(self, ed):
        if len(ed):
            self.ed = float(ed)

    def read_Re(self, Re):
        if len(Re):
            self.Re = float(Re)

    def fs_of(self, x, Re, ed_ratio):
        """
        Reuturns functional value and derivative of f(x) at given x.
        """
        c = 2.00
        a = ed_ratio / 3.7
        b = 2.51 / Re
        term1 = a + b / (x**0.5)

        fn_x = c * log10(term1) + x**(-0.5) 
        fn_prime = (-1/2) * x**(-3/2) - (c*b/2) * x**(-3/2) / term1

        return fn_x, fn_prime

    def calculate_f(self):
        
        if self.Re <= 2000:
            self.f =  f"{64/self.Re:.3f}"
            return 

        f = lambda x: self.fs_of(x, self.Re, self.ed)[0]
        fp = lambda x: self.fs_of(x, self.Re, self.ed)[1]

        # print("Iteration\tprecision\t\tx")
        x_n = INITIAL_GUESS
        count = 0
        while True:
            x = x_n

            x_n = x_n - f(x) / fp(x)
            count +=1

            error = abs(x_n - x)
            # print(f"{count}\t\t{error:.5f}\t\t{x_n:.3f}")

            if error < PRECISION:
                break
        
        self.f =  f"{x_n:.3f}"
        return



if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("Usage: python ffacotr.py [Re] [e/d]")
    else:
        Re = float(sys.argv[1])
        ed_ratio = float(sys.argv[2])

    # print(calculate_f(Re, ed_ratio))
