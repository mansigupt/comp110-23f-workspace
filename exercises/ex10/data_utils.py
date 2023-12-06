"""Dictionary related utility functions."""

__author__ = "730391057"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    column_table: dict[str, list[str]] = {}
    columns: dict[str, str] = table[0]
    # Populate the dictionary with column names and their respective values
    for column in columns:
        values = column_values(table, column)
        column_table[column] = values
    return column_table


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    # Loop through each column in the first row of the table
    for column in table.keys():
        values_head = []
        # Loop through the first number of items of the column
        for value in table[column][:num]:
            values_head.append(value)
        # Assign the list of column values to the result dictionary
        result[column] = values_head
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    # Loop through each column in the second parameter of the function
    for column in columns:
        # Assign to the column key of the result dictionary the list of values from the input dictionary
        result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1.keys():
        result[column] = table1[column]
    for column in table2.keys():
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the frequencies of values in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result