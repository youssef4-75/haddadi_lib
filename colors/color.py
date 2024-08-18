


from typing import Any


def c(n):
    return min(max(0, n), 255)

class _ColorRGB:
    def __init__(self, R, G, B) -> None:
        self.r = R 
        self.g = G 
        self.b = B 

class _ColorRGBA:
    def __init__(self, R, G, B, A) -> None:
        self.r = R
        self.g = G
        self.b = B
        self.a = A

class _ColorHSB:
    def __init__(self, H, S, V) -> None:
        self.h = H
        self.s = S
        self.v = V
        




class Color:
    """class to use colors more efficiently"""
    def __init__(self, R=255, G=255, B=255, p=1) -> None:
        self.R, self.G, self.B, self.p = c(R), c(G), c(B), p

    def __repr__(self) -> str:
        return f"Color({self.R}, {self.G}, {self.B}, p = {self.p})"

    def __add__(self, Col):
        f=[]; h=self.p; o=Col.p
        for i in range(3):f+=[((h*self.get(i)**2+o*Col.get(i)**2)/(h+o))**(1/2)]
        return Color(f[0],f[1],f[2])

    def __rmul__(self, p):
        return Color(R=self.R,G=self.G,B=self.B,p=self.p*p)

    def __sub__(self, other):
        return Color(R=(self.R-other.R)%255,G=(self.G-other.G)%255
            ,B=(self.B-other.B)%255,p=(self.p-other.p))

    def __rotate(self):
        self.R,self.G,self.B=self.G,self.B,self.R,
    
    def __call__(self) -> Any:
        return (self.R, self.G, self.B) 

    def HSV(self):
        pass


    def rotate(self, p=0):
        self.__rotate()
        if p==1:self.__rotate()

    def get(self, n):
        if n==0:return self.R
        if n==1:return self.G
        return self.B

    def color_ify(self, p=None, color = (255, 255, 255)):
        if p:l = p**(1/2)
        else:l = self.p**(1/2)
        a = [(1 - l) * c for c in color]
        self.R = a[0] + l*self.R ;self.G = a[1] + l*self.G ;self.B = a[2] + l*self.B
        
    @classmethod
    def black(cls, p = 1):return cls(0,0,0,p)

    @classmethod
    def red(cls, p = 1):return cls(255,0,0,p)

    @classmethod
    def green(cls, p = 1):return cls(0,255,0,p)

    @classmethod
    def blue(cls, p = 1):return cls(0,0,255,p)

    @classmethod
    def yellow(cls, p = 1):return cls(255,255,0,p)

