#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_test.txt',"r") as text_t:

    content = text_t.readlines()
    print(f'Количество строк в файле - {len(content)} ')
    for j,i in enumerate(content):
        print(f"В {j+1} строке  {len(content[j].split())} слов")



