#딕셔너리를 선업합니다.
disctionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin":"필리핀"
}

#출력합니다.
print("name:", disctionary["name"])
print("type:", disctionary["type"])
print("ingredient:", disctionary["ingredient"])
print("origin:", disctionary["origin"])
print()

#값을 변경 합니다.
disctionary["name"] = "3D 건조 망고"
print("name:", disctionary["name"])