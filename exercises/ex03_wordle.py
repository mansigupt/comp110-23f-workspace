"""EX03 - Structured Wordle!"""
__author__ = "730391057"

def contains_char(search_word: str, find_char: str)-> bool:
    """Determining if a single character is part of the word."""
    assert len(find_char) == 1
    word_idx: int = 0
    while word_idx < len(search_word):
        if search_word[word_idx] == find_char:
            return True
        word_idx += 1
    
    return False  
