import datetime
hi = input("입력: ")
hi = str(hi)
time = datetime.datetime.now()

if hi in ['안녕하세요', '안녕']:
    print("안녕하세요")
elif hi =='지금 몇 시야?' or hi == '지금 몇 시예요?':
    print(f"지금은 {time.hour}시입니다.")
else:
    print(hi)