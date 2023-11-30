"""Dictionary related utility functions."""

__author__ = "730391057"

from io import TextIOWrapper
import csv

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as a dictionary."""
    rows: list[dict[str, str]] = []
    file_handle: TextIOWrapper = open(filename, "r")
    for line in file_handle:
        line = line.strip()
        rows.append(line)
    file_handle.close()
    return rows

