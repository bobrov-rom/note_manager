userName = input ("Введите Имя пользователя: ")
content = input ("Введите описание заметки: ")
status = input ("Введите статус заметки ('создано','в работе', 'готово' ): ")
createdDate = input ("Введите дату начала в формате \"день-месяц-год\": ")
issueDate = input ("Введите дату окончанияв формате \"день-месяц-год\": ")
title = input ("Введите заголовок заметки: ")
subTitile = input ("Введите подзоголовок заметки: ")
note ={
    'userName':userName,'content':content,'status':status,'createdDate':createdDate[:5],'issueDate':issueDate[:5], "titles":
    [title, subTitile]
}
print(note)
