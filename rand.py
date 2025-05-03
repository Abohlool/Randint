from time import time


def main():
    l = list()
    randlist(l)
    random_number = randint(int(input(": ")), l)
    print(random_number)
    
def randint(n: int, l: list) -> int:
    return round(mean(l) * 100 * (10 ** n))    


def randlist(l: list):
    for i in range(1000, 10000, 1000):
        l.append(times(i))


def times(n: int) -> float:
    t1 = time()
    fib(n)
    t2 = time()
    return t2 - t1


def mean(l: list):
    sum: float = 0
    for i in l:
        sum += i
    return sum / len(l)

def fib(n: int, memo=dict()) -> int:
    if (n in memo):
        return memo[n]
    if (n <= 2):
        return 1
    memo[n] = fib(n - 1 ,memo) + fib(n - 2, memo)
    return memo[n]
    
if __name__ == "__main__":
    main()
