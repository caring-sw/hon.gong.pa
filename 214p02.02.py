numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]


for number in numbers:
    if len(str(number)) == 1:
        print(f"{number} 는 1 자리수입니다.")
    elif len(str(number)) == 2:
        print(f"{number} 는 2 자리수입니다.")
    else :
        print(f"{number} 는 3 자리수입니다.")
    