# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#출력합니다
print(f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 \
{now.minute}분 \
{now.second}초")