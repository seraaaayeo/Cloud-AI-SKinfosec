#dic
ais1 = {"key": "val", "key2": "val2"}
ais2 = {"name": "Dasol", "age": "26"}
ais3 = {"name": "Sera", "age": "24"}
ais = [ais1, ais2, ais3]

#enumerate()
print(list(enumerate(ais)))

for i, val in enumerate(ais):
    print("{}번째: {}".format(i, val))

#items()
print(ais1.items())

for i in ais2.items():
    print("element: ", i)
for key, value in ais2.items():
    print("key: {}, val: {}".format(key, value))