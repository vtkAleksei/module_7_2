def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    dict_str = {}
    number_line = 1
    for string in strings:
        key = tuple([number_line, file.tell()])
        dict_str [key] = string
        file.write(string + '\n')
        number_line += 1
    file.close()
    return dict_str


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)