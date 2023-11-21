"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730391057"


class Simpy:
    """Utility class for numerical operations."""
    def __init__(self, values: list[float]) -> None:
        """Constructor for Simpy."""
        self.values = values

    def __str__(self) -> str:
        """String representation of the Simpy object."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, num_values: int) -> None:
        """Fill the Simpy object with a specified value for a given number of times."""
        self.values = [value] * num_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a range of values from start to stop with a specified step."""
        assert step != 0.0 
        self.values = []
        current_value = start
        while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
            self.values.append(current_value)
            current_value += step
        return self
        
    def sum(self) -> float:
        """Calculate the sum of values in the Simpy object."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add a Simpy object or float to the current Simpy object."""
        if isinstance(rhs, Simpy):
            min_len = min(len(self.values), len(rhs.values))
            result_values = [self.values[i] + rhs.values[i] for i in range(min_len)]
        elif isinstance(rhs, float):
            result_values = [x + rhs for x in self.values]
        
        return Simpy(result_values)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise each element in the Simpy object to the power of the corresponding element in another Simpy object or float."""
        if isinstance(rhs, Simpy):
            result_values = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            result_values = [x ** rhs for x in self.values]
        return Simpy(result_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compare the Simpy object with another Simpy object or float for equality."""
        if isinstance(rhs, Simpy):
            min_length = min(len(self.values), len(rhs.values))
            return [self.values[i] == rhs.values[i] for i in range(min_length)]
        elif isinstance(rhs, float):
            return [x == rhs for x in self.values]
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compare the Simpy object with another Simpy object or float for greater than."""
        if isinstance(rhs, Simpy):
            min_length = min(len(self.values), len(rhs.values))
            return [self.values[i] > rhs.values[i] for i in range(min_length)]
        elif isinstance(rhs, float):
            return [x > rhs for x in self.values]
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Retrieve an element or create a new Simpy object using indexing or boolean masking."""
        return self.values[rhs]
    