userName = input ("Введите Имя пользователя: ")
content = input ("Введите описание заметки: ")
status = input ("Введите статус заметки ('создано','в работе', 'готово' ): ")
createdDate = input ("Введите дату начала в формате \"день-месяц-год\": ")
issueDate = input ("Введите дату окончанияв формате \"день-месяц-год\": ")
title = input ("Введите заголовок заметки: ")
subTitile = input ("Введите подзоголовок заметки: ")
note = {
    'Имя':userName,'Описание':content,'Статус':status,'Дата создания':createdDate[:5],'Дата завершения':issueDate[:5],
    "Заголовки":[title, subTitile]
}
for key, value in note.items():
    print("{0}:{1}".format(key, value))

