def convert_2_to_3(n):
    convert_3 = []
    for i in n:
        sum = 0
        for a in range(0, len(i)):
            sum += int(i[-a-1]) * pow(2, a)
        result = sum
        convert_3.append(result)
    return convert_10_to_3(convert_3)


def convert_10_to_3(n):
    convert_3 = []
    for i in n:
        converter = ''
        if i == 0:
            converter = str(0) + converter
        div = i
        while div > 0:
            if div != 0:
                converter = str(div % 3) + converter
                div = div // 3
        convert_3.append(converter)
    return convert_3


def test():
    n = ['000', '001', '010', '011', '100', '101', '110', '111']
    print(convert_2_to_3(n))
    #n = ['000110', '000111', '001000']
    #print(convert_2_to_10(n))


def main():
    test()
    # model()


if __name__ == "__main__":
    main()
