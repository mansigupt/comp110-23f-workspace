"""Challenge Question 7."""
from __future__ import annotations
__author__ = "730391057"


class Point:
    """Making a new class called point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Increasing my number."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Return a point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Setting a str operator."""
        output: str = (f"x: {self.x}; y: {self.y}")  
        return output 
    
    def __mul__(self, factor: int | float) -> Point:
        """Setting a mul operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Setting an add operator overload."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point