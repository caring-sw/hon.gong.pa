numbers = [1, 2, 2, 3, 1]
counter = {}
print(f"현재 숫자: {numbers}")
print()
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
    