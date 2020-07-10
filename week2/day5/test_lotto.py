import random

def lotto():
    lotto = []
    for i in range(6):
        lotto.append(random.randint(1, 46))
    return lotto

def main():
    print(f"lotto number: {lotto()}")

if __name__ == "__main__":
    main()
