# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ser = Character('Серёжа', color="#c8ffc8")
define nad = Character('Надя', color="#c8ffc8")
define er = Character('Эрик', color="#c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    "ХВАТИТ ЭТО ТЕРПЕТЬ!"
    return
