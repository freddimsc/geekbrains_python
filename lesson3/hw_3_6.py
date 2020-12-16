#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def int_func(text):
    return text.capitalize()



def int_func1(text):
    a = []
    for i in range(len(text)):
        a.append(text[i].capitalize())
    return ' '.join(a)

#print(int_func(input('Введите слово: ')))

#print(int_func1(input('Введите слова через пробел: ').split()))

#Решение препода

def int_word(word):
    return word.capitalize()

word_string = input('Введите слова через пробел: ')
print(' '.join(map(int_word,word_string.split())))


