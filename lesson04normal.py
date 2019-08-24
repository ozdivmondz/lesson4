# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

name = str(input('Enter your name: '))

last_name = str(input('Enter your last name: '))

email = input('Enter your email: ')

name_pattern = re.compile(r'[A-Z]')

email_pattern = re.compile(r'[a-z0-9_]+@[a-z]+\.(ru|org|net|com)')


result = name_pattern.search(name)

result1 = name_pattern.search(last_name)

result2 = re.match(email_pattern, email)

if result and result1 and result2:
    print(name, last_name, email, '-', 'the info you entered is valid')
elif result and result2 and not result1:
    print(name, last_name, email,  '-', 'Your last name doesnt have an uppercase letter!')
elif result1 and result2 and not result:
    print(name, last_name, email,  '-', 'Your first name doesnt have a lowercase letter!')
elif result and result1 and not result2:
    print(name, last_name, email, '-', 'The email you have entered is incorrect! example: example123@gmail.com')


# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern = re.compile(r"\.{2,}")

result = re.search(pattern, some_str)

print('Имеется больше одной точки подряд!' if result else 'Нету более одной точки подряд')


# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!