#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('numb_text.txt', 'r') as num_obj:
    content = num_obj.read().split('\n')
    for i in content:
        i = i.split(' ', 1)
        new_list.append(f'{rus[i[0]]}  {i[1]}\n')

with open('numb_text_new.txt', 'w') as num_obj2:
    num_obj2.writelines(new_list)