class Complex:
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a
    def set_b(self, b):
        self.b = b

    def get_complex(self):
        return f"Complex number is {self.a}+{self.b}i"
    def get_real(self):
        return f"Real part is {self.a}"
    def get_imaginary(self):
        return f"Imaginary part is {self.b}i"

complex1 = Complex(3,2)
print(complex1.get_complex())

complex1.set_a(5)
complex1.set_b(3)
print(complex1.get_complex())
print(complex1.get_real())
print(complex1.get_imaginary())


    
