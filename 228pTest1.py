a = str.lower(input("원하는 문자를 입력 하세요!: ")).replace(" ", "")
counter = {}

for key in a:
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1

print(counter)