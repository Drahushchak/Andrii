# coding=utf-8
def rozr(r):
    a = GrayCode(r)
    result = list(a.generate_gray())
    return result


def from_binary_to_gray(code):
    res = list()
    e = list(bin(code)[2:])
    print(e)
    res.append(int(e[0]))
    for i in range(1, len(e)):
        res.append(int(e[i-1])+int(e[i]))
        if res[i] == 2:
            res[i] = 0
    return res


def from_gray_to_binary(codee):
    res = list()
    res.append(int(codee[0]))
    for i in range(1, len(codee)):
        res.append(int(res[i-1]+codee[i]))
        if res[i] == 2:
            res[i] = 0
    return res


if __name__ == "__main__":
    try:
        # print("Розрядність:")
        r = int(input("Розряд кода: "))  # Вводиться n-біт коду Грея
        print(rozr(r))
    except ValueError:
        print("Не правильно введені дані")
        print("---------------------------")
        r = int(input("Розряд кода: "))  # Вводиться n-біт коду Грея
        print(rozr(r))
    except ValueError:
        print("Занадто велике значення")
    finally:
        print("END")
        print()
        close = 0
        while close < 2:
            b = int(input("Число: "))
            print(" - З бінарного кода в код Грея")
            z = from_binary_to_gray(b)
            print(z)
            print()
            print(" - З кода Грея в бінарний код")
            print(from_gray_to_binary(z))
