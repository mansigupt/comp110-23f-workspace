"""Quiz03 practice: christmas edition."""

from __future__ import annotations

class ChristmasTreeFarm:
    """A christmas tree farm!"""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        """Constructor to set up farm."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 0
    
    def plant(self, plot_idx: int) -> None:
        """Plants a tree at a given plot number."""
        self.plots[plot_idx] = 1

    def growth(self) -> None:
        """Grows each planted tree"""
        i: int = 0
        while i < self.plots:
            if self.plots[i] != 1:
                self.plots[i] += 1
            i += 1

    def harvest(self, replant: bool) -> int:
        """Harvest trees that are fully grown."""
        total_trees: int = 0
        i: int = 0

        while i < len(self.plots):
            if self.plots[i] >= 5:
                total_trees += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
        i += 1

        return total_trees
    
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overload addition to create new ChristmasTreeFarm."""
        trees: int = 0
        for plot in self.plots:
            if plot > 0:
                trees += 1
        for plot in rhs.plots:
            if plot > 0:
                trees += 1
        
        return ChristmasTreeFarm(len(self.plots) + len(rhs.plots), trees)