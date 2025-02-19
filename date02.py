# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()
a = now.month

print(f"오늘은 {a}월 입니다.")

# 오전 구분
if now.hour < 12:
    print(f"현재 시각은 {now.hour}시로 오전 입니다.")

# 오후 구분
if now.hour >= 12:
    print(f"현재 시각은 {now.hour}시로 오후 입니다.")
