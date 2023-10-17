pets: list[str] = ["Louis", "Bo", "Bear"]
for pet_name in pets:
    print(f"Good boy, {pet_name}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0,len(names)):
    elem: str = names[idx]
    # print(f"{idx}: {elem}")
    """or"""
    print(f"{idx}: {names[idx]}")