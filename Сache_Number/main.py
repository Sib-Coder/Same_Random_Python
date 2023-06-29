from functools import lru_cache
import time

@lru_cache(100)
def test(num):
    sum =0
    for i in range(num):
        sum = sum + num
    return sum


def progon(mas ):
    for i in mas:
        clerform(i)


def clerform(i):
    print("Блок с цифрами для вызова")
    print(i)
    start = time.time()
    test(i)
    end = time.time()
    print(end - start)


def main():
    mas = [100000, 2000000, 30000000, 4000000, 50000, 60000, 700000, 8000000, 90000000]
    progon(mas)
    clerform(90000000)


if __name__ == "__main__":
    main()