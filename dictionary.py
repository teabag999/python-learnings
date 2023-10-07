# dic = {
#     "Harry": "Code with harry",
#     "Spoon": "Object in kitchen"
# }
#
# print(dic["Harry"])
# print(dic["Spoon"])
#
# info = {
#     'name':'Karan', 'age':19, 'eligible':True
# }
# print(info['name'])
# print(info.get('name2'))
# print(info.keys())
# print(info.values())
#
# for key in info.keys():
#     print(info[key])


ep1 = {100: 46, 200: 60, 300: 55, 400: 85, 500: 99}
ep2 = {600: 67, 700: 50}
# ep1.update(ep2)
# ep1.clear()
# ep1.pop(100)
ep1.popitem()
del ep1[100]
print(ep1)

empty_dict = {}
print(empty_dict)
