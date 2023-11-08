def main() -> None:
    factorials: dict[int,int] = {}
    factorials[3] = factorial(3)
    factorials[4] = factorial(4)
    print(factorials)

def factorial(input: int) -> int:
    answer: int = 1
    for i in range(1, input+1):
        answer *= i
    return answer

if __name__ == "__main__":
    main ()