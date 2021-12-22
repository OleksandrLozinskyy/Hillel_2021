import os

def dir_listing(path: str) -> None:
    '''
    Функция принимает на вход произвольный путь к директории и выводит
    в консоль ее листниг, включая вложенные директории
    :param path: Путь к корневой директории, листинг которой нужно вывести
    в консоль
    :return None: Функция направляет весь вывод в консоль.
    '''

    for root, dirs, files in os.walk(path):
        # Считаем количество слешей в пути, чтоб определить уровень вложения
        level = root.replace(path, '').count(os.sep) 
        # Сдвиг для основного уровня
        indent = ' ' * 4 * (level) 
        # Сдвиг для последующего уровня уровня
        subindent = ' ' * 4 * (level + 1)
        print('{0}{1}/'.format(indent, os.path.basename(root)))
        for f in files:
            print('{0}{1}'.format(subindent, f))


dir_listing('.')