"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730391057"


class Simpy:
    def __init__(self, values: list[float]) -> None:
        self.values = values

    def __str__(self) -> str:
        return (f"Simpy({self.values}")
    
    def fill(self, value: float, num_values: int) -> None:
        self.values = value * num_values
        return self

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0, "Step cannot be 0.0"
        self.values = []
        current_value = start
        while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
            self.values.append(current_value)
            current_value += step
        return self
        
    def sum(self) -> float:
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        if isinstance(rhs, Simpy):
            return Simpy(self.values + rhs.values)
        elif isinstance(rhs, float):
            return Simpy([x + rhs for x in self.values])
        else:
            raise TypeError(f"Unsupported type for addition: {type(rhs)}")
        
    def __pow__(self, rhs: Union[float, Simpy]) -> 'Simpy':
        if isinstance(rhs, Simpy):
            result_values = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            result_values = [x ** rhs for x in self.values]
        return Simpy(result_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        if isinstance(rhs, Simpy):
            min_length = min(len(self.values), len(rhs.values))
            return [self.values[i] == rhs.values[i] for i in range(min_length)]
        elif isinstance(rhs, float):
            return [x == rhs for x in self.values]
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        if isinstance(rhs, Simpy):
            min_length = min(len(self.values), len(rhs.values))
            return [self.values[i] > rhs.values[i] for i in range(min_length)]
        elif isinstance(rhs, float):
            return [x > rhs for x in self.values]
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        return self.values[rhs]
    