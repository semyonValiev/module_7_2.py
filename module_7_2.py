from pprint import pprint

def custom_write(file_name, strings):  #функция принимает file_name - название файла для записи,
    # strings - список строк для записи
    #Записываут в файл file_name все строки из списка strings, каждая на новой строке.
    strings_position = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i, j in enumerate(strings):
        key = (i+1, file.tell())
        strings_position[key] = j
        file.write(j + '\n')
    file.close()
    return strings_position  #Возвращаtn словарь strings_positions,
    # где ключ кортеж (<номер строки>, <байт начала строки>), а значение - записываемая строка
def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

if __name__ == '__main__':
    main()

