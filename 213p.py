# 원본 리스트 선언
original_list = [0, 1, 2, 3, 4, 5, 6, 7]

# 1. extend()
list_a = original_list.copy()
list_a.extend(list_a)
print("1. extend():", list_a)

# 2. append(10)
list_a = original_list.copy()
list_a.append(10)
print("2. append(10):", list_a)

# 3. insert(3, 0)
list_a = original_list.copy()
list_a.insert(3, 0)
print("3. insert(3, 0):", list_a)

# 4. remove(3)
list_a = original_list.copy()
list_a.remove(3)
print("4. remove(3):", list_a)

# 5. pop(3)
list_a = original_list.copy()
list_a.pop(3)
print("5. pop(3):", list_a)

# 6. clear()
list_a = original_list.copy()
list_a.clear()
print("6. clear():", list_a)
