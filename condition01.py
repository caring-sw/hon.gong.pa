# 입력을 받습니다다.
number = input("정수 입력 : ")

#마지막 자리 숫자 추출
last_character = number[-1]

#숫자로 변환하기
last_character = int(last_character)

#짝수 확인
if last_character == 0 \
    or last_character == 2 \
    or last_character == 4 \
    or last_character == 6 \
    or last_character == 8 :
    print("짝수 입니다.")

else :
        print("홀수 입니다.")