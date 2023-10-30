"""Return a a list of short words."""
__author__ = "730391057"


def short_words(list1: list[str]) -> list[str]:
    """Return a list of words that are shorter than 5 characters."""
    short_list: list[str] = []
    i: int = 0
    while i < len(list1):
        if len(list1[i]) < 5:
            short_list.append(list1[i])
        else:
            print(f"{list1[i]} is too long!")
        i += 1
    return short_list


my_list: list[str] = ["sun", "cloud", "sky"]
print(short_words(my_list))