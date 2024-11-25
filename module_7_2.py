strings = ['Текст для tell', 'Use utf-8', 'Потому что два языка', 'Thanks!', 'Raketa']
file_name = 'test.txt'
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    n_pos = []
    n_string = []
    keys = []
    for i in range(len(strings)):
        pos = (file.tell())
        file.write(strings[i] + '\n')
        n_pos.append(pos)
        n_string.append(1 + i)
    file.close()
    for i in range(len(n_string)):
        key = (n_string[i], n_pos[i])
        keys.append(key)
    strings_positions = dict(zip(keys, strings))
    return strings_positions

result = custom_write('test.txt', strings)
for elem in result.items():
    print(elem)



