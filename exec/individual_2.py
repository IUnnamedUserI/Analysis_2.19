import os
import argparse


def tree(path, level, max_levels, show_hidden):
    """
    Вывод списка каталогов и файлов по указанному пути,
    аналогично утилите tree в ОС Linux
    """
    if level > max_levels:
        return
    
    for element in os.listdir(path):
        if not show_hidden and element.startswith('.'):
            continue

        dir = os.path.join(path, element)
        if os.path.isdir(dir):
            print('  ' * level + f'/{element}')
            tree(dir, level + 1, max_levels, show_hidden)

        else:
            print('  ' * level + element)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help="Директория"
    )

    parser.add_argument(
        '-l',
        '--level',
        type=int,
        default=float('inf')
    )

    parser.add_argument(
        '-a',
        '--all',
        action='store_true',
        help="Вывод скрытых файлов"
    )

    parser.add_argument(
        'author',
        nargs='?',
        const=True,
        help="Вывод автора программы"
    )

    args = parser.parse_args()

    if args.author is None:
        print(f'> Автор работы: Иващенко О.А.\n')
        return

    path = os.path.abspath(args.directory)
    if not os.path.exists(path):
        print("Указанного каталога не существует")
        return
    
    if not os.path.isdir(path):
        print(f"Ошибка: {path} - не каталог")
        return
    
    print(f'Список файлов в каталоге {path}')
    tree(path, 0, args.level, args.all)


if __name__ == "__main__":
    main()
    