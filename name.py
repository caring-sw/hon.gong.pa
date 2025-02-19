

while True:
    name = input("이름을 입력하세요: ")
    name = str(name)
    if name == '종료':
        print("프로그램을 종료합니다")
        break

    if  '재효' in name:
        print("박재효는 쿰척 입니다.")
    elif name == '쿰척':
        print("박재효 = 쿰척")    
    elif name == '박영헌':
        print("박영헌은 딴또 입니다.")
    elif name == '딴또':
        print("박영헌 = 딴또")
    elif name == '최성우':
        print("천재")
    else:
        print(f"{name} 는 이름이 아닙니다. 제대로 된 이름을 입력하세요")
