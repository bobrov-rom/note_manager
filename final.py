user_name = input("Введите Имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('создано','в работе', 'готово' ): ")
created_date = input("Введите дату начала в формате \"день-месяц-год\": ")
issue_date = input("Введите дату окончанияв формате \"день-месяц-год\": ")
title = input("Введите заголовок заметки: ")
sub_titile = input("Введите подзоголовок заметки: ")
note = {
    'Имя': user_name, 'Описание': content, 'Статус': status, 'Дата создания': created_date[:5], 'Дата завершения': issue_date[:5],
    "Заголовки": [title, sub_titile]
}
for key, value in note.items():
    print("{0}:{1}".format(key, value))

