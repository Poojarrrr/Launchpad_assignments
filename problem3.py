values = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
print("list: " +str(values))

result = [i for i in range(len(values)) if values[i] == 2 ]

print(str(result))