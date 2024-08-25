def custom_write(file_name, string):
    strings_positions = {}

    with open(file_name, 'w', encoding = 'utf - 8') as file:
        for line_number, string in enumerate(string):
            byte_positions = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number + 1, byte_positions)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

