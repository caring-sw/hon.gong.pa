int_0 = input("정수를 입력해 주세요: ")

int_1 = int(int_0)
int_2 = int(int_1)%2
int_3 = int(int_1)%3
int_4 = int(int_1)%4
int_5 = int(int_1)%5

if int_2 == 0:
    print (f"{int_1}은 2로 나누어 떨어지는 숫자 입니다.")
elif int_2 != 0:
    print (f"{int_1}은  2로 나누어 떨어지는 숫자가 아닙니다.")
if int_3 == 0:
    print (f"{int_1}은 3으로 나누어 떨어지는 숫자 입니다.")
elif int_3 != 0:
    print (f"{int_1}은  3으로 나누어 떨어지는 숫자가 아닙니다.")
if int_4 == 0:
    print (f"{int_1}은 4로 나누어 떨어지는 숫자 입니다.")
elif int_4 != 0:
    print (f"{int_1}은  4로 나누어 떨어지는 숫자가 아닙니다.")
if int_5 == 0:
    print (f"{int_1}은 5로 나누어 떨어지는 숫자 입니다.")
elif int_5 != 0:
    print (f"{int_1}은  5로 나누어 떨어지는 숫자가 아닙니다.")