"""Node Class for a linked list."""

from __future__ import annotations

__author__ = "730391057"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct a Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int: 
        """Return the data of last element in the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data