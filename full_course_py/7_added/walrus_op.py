walrus = False
print(walrus)

print(walrus := True)
print(walrus)

for i in range(rows := int(input('enter rows: '))):
    print('*' * (i + 1))
