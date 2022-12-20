from data import com_name, directories
from call import func


if __name__ == '__main__':
    while True:
        command = input('\nВведите команду: ')
        if command == 'q':
            print('Завершение программы...')
            break
        elif command not in com_name:
            print('Такой команды не существует! Попробуйте ещё раз')
        else:
            func(command)

