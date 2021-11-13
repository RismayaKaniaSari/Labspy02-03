data = []
for i in range(5):
    x = int(input('Masukan bilangan: '))
    data.append(x)
print('Data sebelum diurutkan: ', data)
list.sort(data)
print('Data setelah diurutkan', data)