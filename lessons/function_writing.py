def short_words(list1: list[str]) -> list[str]:
    """Filter out short words"""
    list2: list[str] = []
    idx: int = 0
    while idx < len(list1):
        if len(list1[idx]) < 5:
            list2.append(list1[idx])
        else:
            print(f"{list1[idx]} is too long!")
        idx += 1

    return list2