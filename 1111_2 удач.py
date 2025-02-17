# Импортируем нужные модули
import vk_api

import random

from spisok import podergka
from vk_api import VkUpload
from vk_api import keyboard
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token='17af1c0974235b71dcd6dac8452aeb6a79acc4c728b12776e3547bb521f6419d5e3e103e7b3bb4eb3d6cd')
vk = vk_session.get_api()
# Работа с сообщениями
longpool = VkLongPoll(vk_session)
upload = VkUpload(vk_session)


# Метод написания сообщения
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {
            "user_id": id,
            "message": some_text,
            "random_id": 0,
            'keyboard': basa()
        }
    )

def variants_choice(id, some_text):
   vk_session.method("messages.send", {
            "user_id": id,
            "message": some_text,
            "random_id": 0,
            'keyboard': trenirovka()
        }
    )

def images_msg(id, url):
    vk.messages.send(
        user_id=id, 
        attachment=url, 
        random_id=0
        )

def send_stick(id,number):
    vk.messages.send(
        user_id=id, 
        sticker_id= number, 
        random_id=0
        )

            
    
def zitat(id,list) :
    vk.messages.send(
        user_id= id, 
        message= list,
        random_id= 0,
        )
def rand (id, url):
	vk.messages.send(
		user_id= id,
		attachment= url,
		
		random_id= 0)



#Клавиатура

def basa():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться
    keyboard.add_button("Инструкция по работе с ботом")
    keyboard.add_line()
    keyboard.add_button("Мотивационная цитата")
    keyboard.add_line()
    keyboard.add_button('Где решать?')
    keyboard.add_line()
    keyboard.add_button('Тренировка' )
 

    #Эта функция используется для закрытия клавиатуры
    return keyboard.get_keyboard()

def trenirovka():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
    keyboard.add_button("Вариант 1")
    keyboard.add_line()
    keyboard.add_button("Вариант 2")
    keyboard.add_line()
    keyboard.add_button("Вариант 3")
    keyboard.add_line()
    keyboard.add_button("Вариант 4")
    keyboard.add_line()
    keyboard.add_button("Вернуться")

    return keyboard.get_keyboard()
# тренировка
pervii = ['photo-209423824_457239049',
'photo-209423824_457239050',
'photo-209423824_457239051',
'photo-209423824_457239052',
'photo-209423824_457239053',
'photo-209423824_457239054',
'photo-209423824_457239055',
]
t1= list (pervii)


# Основной цикл
for event in longpool.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW and event.text:
        if event.to_me:   # Если оно имеет метку для меня( то есть бота)
            if event.from_user: # если сообщение пришло от челика
                msg = event.text
                id = event.user_id
                

                if msg == "Мотивационная цитата":
                    zitat(id, random.choice(podergka) )
                    send_stick(id, 4276)

                elif msg == "Инструкция по работе с ботом":
                    send_some_msg(id, 'Напиши номер задания ЕГЭ по информатике, чтобы получить план его решения')

                elif msg == 'Где решать?':#
                    send_some_msg(id, 'Лучшими сайтами для прорешивания вариантов являются:\n Открытый банк заданий ЕГЭ;\n Сайт Полякова в разделе ЕГЭ, там можно выбрать номера и подвиды номеров, а потом проверить ответ на сайте; \n Решу ЕГЭ, где можно решать как сами варианты, так и номера с подвидами и решением.')

                elif msg == "1":#
                    send_some_msg(id, 'Структурирование информации — это установление главных элементов в информационных сообщениях и установление связей между ними.')
                    images_msg(id, "photo-209423824_457239018")
                    send_some_msg(id, 'Мы с Вами видим следующую картину: даны граф и таблица, отражающие одно и то же событие, но в таблице пункты пронумерованы, а в графе - подписаны.\n Т.е. задание сводится к тому, что мы должны соотнести пункты из таблицы и графа. Иногда требуется соотнести все пункты, иногда достаточно 3-4, зависит от условия задачи и вопроса.\n Внимательно читаем вопрос: Сумма протяжённостей дорог из пункта Б в пункт В и из пункта Г в пункт Д')
                    images_msg(id, "photo-209423824_457239019")
                    send_some_msg(id, 'Начать стоит с того, что граф симметричен.\n Запомним этот момент.\n Далее, начинаем с того пункта, который отличается от всех остальных. В данном случае это пункт К - имеет целых 6 рёбер. Нетрудно догадаться, что в таблице ему соответсвует пункт под номером 5. Подписываем.')
                    images_msg(id, "photo-209423824_457239020")
                    send_some_msg(id, 'Также заметим, что пункты А и Е имеют по 2 вхождения, что отличает их от остальных. Это пункты 1 и 3 в таблице. Но как быть: пункт А может быть как первым, так и третьим?\n Без паники, вспоминаем симметричность графа. Задание построено таким образом, что мы можем взять любую комбинацию. Заметьте, что ответ на вопрос задачи (сумма длин БВ и ГД) не изменится, если мы поменяем местами А и Е.\n Тут уже на Ваш выбор. Например, я возьму пункт А за первый в таблице, а пункт Е - за третий.')
                    images_msg(id, "photo-209423824_457239021")
                    send_some_msg(id, 'Что делать теперь? Оставшиеся 4 пункта имеют по 3 дороги каждый. Значит, отличить таким образом мы их не сможем. Но зато можем провести анализ их соседей. Например, пункты Б и Д соединяются с А и Е соответственно. Из таблицы видно, что с пунктом А соединяется второй пункт, т.к. на пересечении строки и столбца стоит цифра. Аналогично вычисляем Д - он четвёртый.')
                    images_msg(id, "photo-209423824_457239022")
                    send_some_msg(id, 'Осталось два пункта. Видим, что В соединён с Б, а Д - с Г. Несложно будет определить их.')
                    images_msg(id, "photo-209423824_457239022")
                    send_some_msg(id, 'Осталось совсем немного. \n Возвращаемся к вопросу задачи. Требовалось определить сумму дорог БВ и ГД. Смотрим пересечения строки Б со столбцом В. Видим число 13. \n (Так как граф неориентированный (нет стрелочек), то можно и наоборот: взять столбец Б и строку В)\n Аналогично находим ГД - 7. Ответом будет сумма этих чисел.')
                    images_msg(id, "photo-209423824_457239023")
                    send_some_msg(id, 'Ответ: 20')
                    
                elif msg == "2":#
                    send_some_msg(id, 'Номер 2 можно решать двумя способами\n 1) Аналитически. Зная алгебру логику, можно построить свою таблицу по заданной функции, а потом соотнести с той, которая дана в задании.\n 2)С помощью кода на Python.')
                    images_msg(id, "photo-209423824_457239024")
                    images_msg(id, "photo-209423824_457239025")
                    send_some_msg(id, 'Таблица истинности алгебры логики:')
                    images_msg(id, "photo-209423824_457239026")
                    images_msg(id, "photo-209423824_457239027")

                elif msg == "3":
                    send_some_msg(id, 'Главная функция в 3 задании- ВПР. \n Выделить ячейку → нажать на Fx (Shift +F3) → выбрать категорию «Ссылки и массивы» → выбрать функцию ВПР → нажать «Ок». После этого открывается окно, где можно заполнить ячейки аргументов формулы. Синтаксис функции ВПР выглядит так:=. ВПР (искомое значение; таблица; номер столбца; интервальный просмотр). \n Так же часто надо работать с сортировкой данных:')
                    images_msg(id, "photo-209423824_457239028")
                    images_msg(id, "photo-209423824_457239029")
                    send_some_msg(id, 'Важно знать полезные функции. \n МАКС() - возврашает наибольшее значение из списка аргументов. Логические и текстовые значения игнорируются. \n МИН() - возврашает наименыпее значение из списка аргументов. Логические и текстовые значения игнорируются. \n СЧЕТ() -подечитывает количество ячеек в диапазоне, который содержит числа. \n СЧЕТЕСЛИ ()-подечитывает количество непустых ячеек в диапазоне, удовлетворяющих заданному условию. \n СЧЕТЕСЛИМН() - подсчитывает количество непустых ячеек в диапазоне, удовлетворяющих заданному набору условий. \n СУММ() - суммирует аргументы. \n СУММЕСЛИ() - суммирует ячейки, заданные указанным условием. \n СУММЕСЛИМН() - суммирует ячейки, удовлетворяющие заданному набору условий. \n СРЗНАЧ() - возвращает среднее арифметическое своих аргументов, которые могут быть числами, именами, массивами или ссылками на ячейки с числами. \n СРЗНАЧЕСЛИ() - вычисляет среднее (арифметическое) для ячеек, заданных указанным условием. \n И() - проверяет, все ли аргументы имеют значение ИСТИНА, и возврашает значение ИСТИНА, если истинны все аргументы. \n ИЛИ() - проверяет, имеет ли хотя бы один из аргументов значение ИСТИНА, н возвращает значение ИСТИНА или ЛОЖЬ. Значение ЛОЖЬ возвращается только в том случае, если все аргументы имеют значение ЛОЖЬ. \n ABS() - возвращает модуль числа\n НАИБОШИЙ () возвращает к-ое наиболыпее значение в множестве данных. \n НАИМЕНЬШИЙ() - возвращает к-ое наименьшее значение в множестве данных. \n КОРЕНЬ() - возвращает квадратный корень. \n ЕСЛИ() - проверяет, выполняется ли условие, и возвращает одно значение, если условие истинно, и другое значение, если условие ложно. \n ')
                    

                elif msg == "4":
                    send_some_msg(id, 'Условие Фано: ни одно кодовое слово не должно являться началом другого кодового слова (что обеспечивает однозначное декодирование сообщений с начала)')
                    send_some_msg(id, 'Префиксный код — это код, в котором ни одно кодовое слово не совпадает с началом другого кодового слова. Сообщения при использовании такого кода декодируются однозначно.\n если сообщение декодируется с конца, то его можно однозначно декодировать, если выполняется обратное условие Фано:')
                    send_some_msg(id, 'Обратное условие Фано: никакое кодовое слово не является окончанием другого кодового слова')
                    send_some_msg(id, 'Постфиксный код — это код, в котором ни одно кодовое слово не совпадает с концом другого кодового слова. Сообщения при использовании такого кода декодируются однозначно и только с конца.')
                    send_some_msg(id, 'Кодирование — это представление информации в форме, удобной для её хранения, передачи и обработки. Правило преобразования информации к такому представлению называется кодом.\n Кодирование бывает равномерным и неравномерным:\n  при равномерном кодировании всем символам соответствуют коды одинаковой длины;\n  при неравномерном кодировании разным символам соответствуют коды разной длины, это затрудняет декодирование.')
                    send_some_msg(id, 'photo-209423824_457239033')
                    images_msg(id, "photo-209423824_457239034")  
                      
                elif msg == "5":
                    images_msg(id, "photo-209423824_457239043")
                    images_msg(id, "photo-209423824_457239044")
                    send_some_msg(id, 'Циклы: \n if/else – если/иначе \n while- пока ')
                    send_some_msg(id, 'Знаки: \n +  - сумма.  Можно складывать числа с числами, строки со строками \n -  - разность. Можно из числа вычесть другое число \n *  - произведение. Можно умножать число на число и число на строку \n ** - степень числа \n / - частное. Можно делить число на число. \n >=  - больше или равно \n<= -  меньше или равно \n ==  - равно \n >  - больше \n < - меньше \n = присваивание ')

                elif msg == "6":
                    send_some_msg(id, 'Переписываем код Python в программу \n Если 1 строчка с input, тогда надо будет работать с кодом или подбирать ответ методом подбора. Работа с кодом показана на картинках, а вот подбор это сокрощение вводных данных для того чтобы результат приближался к нужному. После каждого запуска программы и вводимого числа, надо снова запускать код(F5) \n Если не с input, тогда просто запускаем программу')
                    images_msg(id, "photo-209423824_457239035")
                    images_msg(id, "photo-209423824_457239036")

                elif msg == "7":
                    images_msg(id, "photo-209423824_457239045")
                    images_msg(id, 'photo-209423824_457239046')
                    

                elif msg == "8":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 12931)
                elif msg == "9":
                    send_some_msg(id, 'Полезные функции. \n МАКС() - возврашает наибольшее значение из списка аргументов. Логические и текстовые значения игнорируются. \n МИН() - возврашает наименыпее значение из списка аргументов. Логические и текстовые значения игнорируются. \n СЧЕТ() -подечитывает количество ячеек в диапазоне, который содержит числа. \n СЧЕТЕСЛИ ()-подечитывает количество непустых ячеек в диапазоне, удовлетворяющих заданному условию. \n СЧЕТЕСЛИМН() - подсчитывает количество непустых ячеек в диапазоне, удовлетворяющих заданному набору условий. \n СУММ() - суммирует аргументы. \n СУММЕСЛИ() - суммирует ячейки, заданные указанным условием. \n СУММЕСЛИМН() - суммирует ячейки, удовлетворяющие заданному набору условий. \n СРЗНАЧ() - возвращает среднее арифметическое своих аргументов, которые могут быть числами, именами, массивами или ссылками на ячейки с числами. \n СРЗНАЧЕСЛИ() - вычисляет среднее (арифметическое) для ячеек, заданных указанным условием. \n И() - проверяет, все ли аргументы имеют значение ИСТИНА, и возврашает значение ИСТИНА, если истинны все аргументы. \n ИЛИ() - проверяет, имеет ли хотя бы один из аргументов значение ИСТИНА, н возвращает значение ИСТИНА или ЛОЖЬ. Значение ЛОЖЬ возвращается только в том случае, если все аргументы имеют значение ЛОЖЬ. \n ABS() - возвращает модуль числа\n НАИБОШИЙ () возвращает к-ое наиболыпее значение в множестве данных. \n НАИМЕНЬШИЙ() - возвращает к-ое наименьшее значение в множестве данных. \n КОРЕНЬ() - возвращает квадратный корень. \n ЕСЛИ() - проверяет, выполняется ли условие, и возвращает одно значение, если условие истинно, и другое значение, если условие ложно.')

                elif msg == "10":
                    send_some_msg(id, 'в разработке')
                elif msg == "11":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 10062)
                elif msg == "12":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 16289)
                elif msg == "13":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 2160)
                elif msg == "14":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 60758)
                elif msg == "15":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 4578)
                elif msg == "16":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 4182)
                elif msg == "17":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 8451)
                elif msg == "18":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 8451)
                elif msg == "хуй" or 'Хуй':
                    send_some_msg(id, 'Сам такой!')
                    send_stick(id, 60535)
                    images_msg(id, 'photo401297847_457280309')
                elif msg == "19":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 10577)
                elif msg == "20":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 12909)
                elif msg == "21":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 12910)
                elif msg == "22":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 13501)
                elif msg == "23":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 20516)
                elif msg == "24":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 5580)
                elif msg == "25":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 10069)
                elif msg == "26":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 12881)
                elif msg == "27":
                    send_some_msg(id, 'в разработке')
                    send_stick(id, 12947)
            
                elif msg =='Привет' :
                    send_some_msg(id, "Привет, мой друг! Я твой помощник по подготовке к ЕГЭ.")
                    send_stick(id, 21)

                elif msg == 'Тренировка':
                    variants_choice(id, 'Выберите вариант')
                    variants_choice(id, 'Для отработки определенного номера, напишите перед ним букву т. Пример: т1. ( Пока доступны 1 номера)')
                elif msg == 'Вариант 1':
                    variants_choice(id,'ссылка на сайт Решу ЕГЭ: https://inf-ege.sdamgia.ru/test?id=9695146')
                elif msg == 'Вариант 2':
                    variants_choice(id,'ссылка на сайт Решу ЕГЭ: https://inf-ege.sdamgia.ru/test?id=9695144')
                elif msg == 'Вариант 3':
                    variants_choice(id,'ссылка на сайт Решу ЕГЭ: https://inf-ege.sdamgia.ru/test?id=9695147')
                elif msg == 'Вариант 4':
                    variants_choice(id,'ссылка на сайт Решу ЕГЭ: https://inf-ege.sdamgia.ru/test?id=9695148')
                elif msg == 'Вернуться':
                    send_some_msg(id,'Что-нибудь ещё?')
                elif msg == 'т1':
                	rand(id, random.choice(t1))
          
                else:
                    send_some_msg(id,'Я тебя не понимаю. Напиши "Привет" ')   




