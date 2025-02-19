# 정수
a = "{}".format("안녕")

# 특정 칸에 출력하기
b = "{:5d}".format(52)
c = "{:10d}".format(-52)

# 빈칸을 0으로 채우기
d = "{:05d}".format(52)
e = "{:05d}".format(-52)

print("# 기본")
print(a)
print("# 특정 칸에 출력하기")
print(b)
print(c)
print("#빈칸을 0으로 채우기")
print(d)
print(e)
 