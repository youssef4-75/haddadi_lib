from dataclasses import dataclass
from typing import Any
from .exceptions import IncompatibleValueError


@dataclass
class Pot[UNIT]:
    def __init__(self, value: UNIT, /, *, unit: str):
        self.value = value
        self.__type = unit
    
    @property
    def unit(self):
        return self.__type

    def __call__(self, method=None, *args: Any, **kwds: Any) -> Any:
        if method: return method(self, *args, **kwds)
        return self.value 
    
    def set(self, value: Any) -> Any:
        self.value = value
    
    def __len__(self):
        return len(self.value)
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __add__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to add pot to pot")
        self.united(other.unit)
        return Pot(self.value + other.value, unit=self.unit)
    
    def __sub__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to sub pot to pot")
        self.united(other.unit)
        return Pot(self.value - other.value, unit=self.unit)
    
    def __mul__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to mul pot to pot")
        self.united(other.unit)
        return Pot(self.value * other.value, unit=self.unit)
    
    def __truediv__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to truediv pot to pot")
        self.united(other.unit)
        if other.value == 0:
            raise ZeroDivisionError("division by zero")
        return Pot(self.value / other.value, unit=self.unit)
    
    def __eq__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value == other.value
    
    def __ne__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value != other.value
    
    def __gt__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value > other.value
    
    def __ge__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value >= other.value
    
    def __lt__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value < other.value
    
    def __le__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to compare pot to pot")
        self.united(other.unit)
        return self.value <= other.value
    
    def __iadd__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to add pot to pot")
        self.united(other.unit)
        self.value += other.value
        return self
    
    def __isub__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to sub pot to pot")
        self.united(other.unit)
        self.value -= other.value
        return self
    
    def __imul__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to mul pot to pot")
        self.united(other.unit)
        self.value *= other.value
        return self
    
    def __itruediv__(self, other):
        if not isinstance(other, Pot):
            raise TypeError("you need to truediv pot to pot")
        self.united(other.unit)
        if other.value == 0:
            raise ZeroDivisionError("division by zero")
        self.value /= other.value
        return self
    
    def __neg__(self):
        self.value = -self.value
        return self
    
    def __getitem__(self, key):
        if key == 0: return self.value
        return self.__type

    def united(self, unit: str, *, test=None):
        if self.unit.upper() != unit.upper():
            raise IncompatibleValueError(unit, self.unit)
        if test is not None and not test(self.value):
            raise ValueError("pot content doesn't verify conditions ")

