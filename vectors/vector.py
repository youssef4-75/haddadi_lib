

from math import cos, sin, atan, pi
from pygame import Rect, Vector2
# from debug import debug, ic



class Vector(Vector2):
    def __init__(self, *L):
        if len(L) == 1 and isinstance(L[0], complex):
            return super().__init__(L[0].real, L[0].imag)
        return super().__init__(*L)

    @classmethod
    def from_rects(cls, R1: Rect, R2: Rect):
        return (cls() + R2.center) - R1.center

    @classmethod
    def from_coords(cls, t1: tuple[int], t2: tuple[int]):
        return (cls() + t2) - t1

    def to_complex(self): return self.x + 1j * self.y

    def attenuate(self, power=1):
        n = self.magnitude()
        if n == 0: return self
        return n**(-power-1) * self
    
    def __add__(self, __value: Vector2):
        return Vector(super().__add__(__value))

    def rotate_(self, _element):
        """in rad"""
        match _element:
            case complex(): return Vector(self.to_complex() * _element)
            case float()|int(): return super().rotate_rad(_element)
            case _: 
                print("here is error")
                return super().rotate(self.angle_to(_element))
    
    def orth(self, n=1): 
        return self.rotate(90*n)

    def normalize_(self, New_length=None, Max_length=None):
        if New_length is None:
            New_length = self.magnitude()
            if New_length == 0: return self.copy()
        if Max_length is not None and New_length > Max_length: New_length = Max_length 
        try: self.scale_to_length(New_length)
        except ValueError: pass
        return self.copy()
    
    
    
    def coordinates(self, base = None):
        if base is None: base = ((1, 0), (0, 1))
        else: 
            base = Vector(base).normalize()
            base = (base, base.orth())
        return (self*base[0], self*base[1])
    
    def filter(self, L) :
        x = y = 0
        if L[0] == '1' and self.x > 0:
            # pass only if right
            x = self.x
        if L[1] == '1' and self.x < 0:
            # pass only if left
            x = self.x
        if L[2] == '1' and self.y > 0:
            # pass only if up
            y = self.y
        if L[3] == '1' and self.y < 0:
            # pass only if down
            y = self.y
        return Vector(x,y)

    @classmethod
    def UP(cls): return cls(0, -1)
    @classmethod
    def DOWN(cls): return cls(0, 1)
    @classmethod
    def LEFT(cls): return cls(-1, 0)
    @classmethod
    def RIGHT(cls): return cls(1, 0)
    @classmethod
    def rot(cls, angle): """in degree""";return cls.from_polar((1, angle))  # in degree 
    
class _Vector(complex):
    @classmethod
    def from_rects(cls, R1: Rect, R2: Rect):  # done
        return cls(R2.centerx - R1.centerx, R2.centery - R1.centery)
    
    @classmethod
    def from_coords(cls, t1: Rect, t2: Rect):
        return cls(t2[0] - t1[0], t2[1] - t1[1])

    def attenuate(self, power=1):
        n = abs(self)
        if n == 0: return self
        return n**(-power-1) * self

    def __rmul__(self, __value):
        return Vector(super().__rmul__(__value))
    
    def __add__(self, __value: complex):
        return Vector(super().__add__(__value))
    
    def __sub__(self, __value: complex):
        return Vector(super().__sub__(__value))
    
    def __mul__(self, __value: complex):
        "here"
        return 1

    def y(self, x=0, pass_positive=False, pass_negative=False):
        if pass_positive and self.imag>=0:return Vector(self.real, self.imag)
        if pass_negative and self.imag<=0:return Vector(self.real, self.imag)
        return Vector(x,self.imag)

    def x(self, y=0, pass_positive=False, pass_negative=False):
        if pass_positive and self.imag>=0:return Vector(self.real, self.imag)
        if pass_negative and self.imag<=0:return Vector(self.real, self.imag)
        return Vector(self.real,y)
    
    def arg(self):
        if self == 0: raise Exception("Calculating argument of zero is impossible.")
        if self.real == 0: return pi if self.imag > 0 else -pi
        return atan(self.imag/self.real) if self.real > 0 else pi - atan(self.imag/self.real)

    def filter(self, L) :
        x = y = 0
        if L[0] and self.real > 0:
            # pass only if right
            x = self.real 
        if L[1] and self.real < 0:
            # pass only if left
            x = self.real
        if L[2] and self.imag > 0:
            # pass only if up
            y = self.imag
        if L[3] and self.imag < 0:
            # pass only if down
            y = self.imag
        return Vector(x,y)

    def proj(self, v) -> float: return self.real*v.real+self.imag*v.imag

    def magnitude(self, p = 2):
        if p == 2:return abs(self)
        else:return (((self.real)**p)+((self.imag)**p))**(1/p)

    def rotate(self, angle):
        return Vector(self*complex(cos(angle), sin(angle)))
    
    def orth(self):
        'its me'
        return Vector(self * complex(0,1))
    
    def normalize_(self,**kwargs):
        if "New_length" in kwargs :
            if (n:=abs(self))!= 0:
                return (kwargs["New_length"]) * Vector(self / n)
        elif "Max_length" in kwargs:
            ML = kwargs["Max_length"]
            n = abs(self)
            if n >= ML:
                return ML/n * Vector(self)
        return Vector(self.real, self.imag)
    
    def coordinates(self, in_base: tuple = None, as_base = None)->tuple[int,int]:
        if in_base:
            pass
        if as_base:
            return (self.real*as_base[0] + self.imag*as_base[1]).coordinates()
        return (self.real,self.imag)
    
    def diff(self,other):return (self-other).abs()

    @classmethod
    def DOWN(cls): return cls(0,1)
    
    @classmethod
    def UP(cls): return cls(0,-1)
    
    @classmethod
    def RIGHT(cls): return cls(1,0)
    
    @classmethod
    def LEFT(cls): return cls(-1,0)
        
    @classmethod
    def rot(cls, angle): return cls(cos(angle),sin(angle))
