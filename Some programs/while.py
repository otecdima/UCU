# sum = 0

# for i in dir(str):
#     if i[0] != '_':
#         sum += 1
# print(sum)

# all_atrr = dir(str)
# all_methods = []
# for item in all_atrr:
#     if not(item.startswith('__')) and not(item.endswith('__')):
#         all_methods.append(item)

# print(len(all_methods))

# lst = [func(i) for i in <sequential> if <condition>]
# lst = [item.upper() for item in dir(str) if not (item.startswith("__") and item.endswith('__'))]
# print(type(lst[12].lower()))

phone = "+1-234-567-89-10"
 
# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)


