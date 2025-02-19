#딕셔너리를 선업합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

#존재하지 않는 키에 접근해 봅니다.
key = input("접근하고 하는 키:")
value = dictionary.get(key)

print("값:", value)

#None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")