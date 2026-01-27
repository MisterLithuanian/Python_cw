import math

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if (y==0): raise ValueError
        self.x = x
        self.y = y
        r = math.gcd( int(self.x), int(self.y) )
        self.x, self.y = self.x // r, self.y // r
        if (self.y < 0): 
            self.y *= -1
            self.x *= -1

    def normalize(self):
        r = math.gcd( int(self.x), int(self.y) )
        self.x, self.y = self.x // r, self.y // r
        if (self.y < 0): 
            self.y *= -1
            self.x *= -1
        return self

    def wspolny_dzielnik(self, frac1, frac2):
        a = Frac(frac1.x * frac2.y, frac1.y * frac2.y)
        b = Frac(frac2.x * frac1.y, frac1.y * frac2.y)
        return a, b


    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        return str(self.x) + (f"/{self.y}" if abs(self.y)!=1 else "")

    def __repr__(self):         # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        if isinstance(other, Frac):
            return self.x == other.x and self.y == other.y
        if isinstance(other, int):
            return self.x == other and self.y == 1
        return False
    
    def __ne__(self, other): 
        return not self == other

    def __lt__(self, other):  #<
        return (self.x*other.y < self.y*other.x)

    def __le__(self, other):  #<=
        return (self.x*other.y <= self.y*other.x)

    def __gt__(self, other): 
        return (self.x*other.y > self.y*other.x)

    def __ge__(self, other): 
        return (self.x*other.y >= self.y*other.x)

    def __add__(self, other):
        if isinstance(other, int):
            return Frac(self.x + other * self.y, self.y)
        if isinstance(other, Frac):
            return Frac(
                self.x * other.y + other.x * self.y,
                self.y * other.y
            )
        
    __radd__ = __add__              # int+frac

    def __sub__(self, other):
        if isinstance(other, int):
            return Frac(self.x - other * self.y, self.y)
        if isinstance(other, Frac):
            return Frac(
                self.x * other.y - other.x * self.y,
                self.y * other.y
            )
        
    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if( isinstance(other, int) ): return Frac( self.x*other, self.y ).normalize()
        if( isinstance(other, Frac) ): return Frac( self.x*other.x, self.y*other.y ).normalize()

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):   # frac1/frac2, frac/int, Py2
        if( isinstance(other, int) ): return Frac( self.x, self.y*other ).normalize()
        if( isinstance(other, Frac) ): return Frac( self.x*other.y, self.y*other.x ).normalize()

    def __rdiv__(self, other):  # int/frac, Py2
        return Frac( self.y*other, self.x ).normalize()

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        if( isinstance(other, int) ): return Frac( self.x, self.y*other ).normalize()
        if( isinstance(other, Frac) ): return Frac( self.x*other.y, self.y*other.x ).normalize()

    def __rtruediv__(self, other):   # int/frac, Py3
        return Frac( self.y*other, self.x ).normalize()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

