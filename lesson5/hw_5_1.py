#1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open('HW_5_1.txt',"w") as text_obj:
    content = input('Введите текст: ')
    while content:
        text_obj.writelines(f'{content}\n')
        content = input('Введите текст: ')
        if not content:
            break
