import vk_api, json
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def get_button(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \""+ "1" + "\"}",
            "label": str(text)
        },
        "color": str(color)
    }
keyboard = 0
def write_msg(user_id, message, keyboard=keyboard):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0, "keyboard": keyboard})

#def write_msg1(user_id, message):
 #   vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})

def warpSymbols(r, e, n):
    o = ""
    symbols = "★彡༒☬☠︎♕乡☬牡マキグナルファ系路克瑞大阪市立学鎰命科ャマ能力ϒ人は妻スティ要通り玉宏¥サ丹谷Ѫ灯影伝鶐♠♡♢♣♤♥♦♧⁂☼☽☾✪✫✬✭✮✯"
    for a in range(random.randint(e, n)):
        o += symbols[random.randint(0, len(symbols) - 1)]
    return o + r + o[::-1]

def generate_damage():
	list1 = ["бездарный", "тупоголовый", "ебанутый", "пизданутый", "безмозглый", "блядский", "отсталый", ""]
	list2 = ["сын шлюхи", "долбаёб", "бездарность", "бездарь", "хуесос", "выблядок", "кусок дерьма", "дегенерат", "уебан"]
	list3 = ["я тебе запрещаю разговаривать", "закрой ебало", "завали ебальник", "у тебя на аве", "у тебя мать шлюха", "с завода", 
	"без будущего", "я лучше тебя в каждом аспекте жизни", "никогда не заходи в эту игру"]
	resultlist = [list1, list2, list3]
	n = ""
	for i in range(3):
		n += resultlist[i][random.randint(0, len(resultlist[i])-1)] + " "
	return n

def generate_rule(i):
    rules = ['1. ты не клоун. если ты ставишь себе на аву гуля, спамишь zxczxczcxczcxzxc, ставишь паузы после каждого кила без причин и просто позер - то это не значит, что ты гуль, и права называть себя им не имеешь',
            '2. тебе должно быть похуй, ты аморал, без нравственных качеств. тебя послали нахуй, сказали что ты бездарь? не позорься, не оправдывайся, не отвечай, хочешь доказать - докажи на деле, уничтожь в zxc, ты не терпила, ты не тратишь свое время. ты обещал разбить вещи? бей их, встань в амулет, отвечай за слова',
            '3. не выeбывaйcя. у тебя 3к птс и ты пuздuшь что смурф? закрой рот, это твой ммр, ты играешь на победу и не присваивай себе заслуг, которых не добился. тебе никто ничего не обязан и ты тоже. если ты ломаешь вещи из за того, что тебе не пикнули саппорта - ты нытик, ты не гуль',
            '4. каждый гуль должен хотя бы знать что такое zxc, а тем более уметь там постоять за себя. если для мужчин нормальна случайность обменяться кулаками с другим мужчиной, то так же норма для гуля ответить или заставить ответить за слова в zxc. не будь тряпкой, ты сильнее'
,           '5. сосредотачивайся на игре, zitraks mod. твоя главная цель победить, ты должен уметь давать all mute, справляться с тильтом и выигрывать непобедимое. враги должны бояться гулей, а не смеяться с рейдж бб нытика'
,           '6. если ты достоин называться гулем, то ты априоре ставишь себя выше остальных. если ты уверен в себе, то забирай роль, фпшь героя, твоя игра - твои правила, но не руинь, пока не заруинили тебе. пикнули дабл мид? иди на сфе в лес и тащи соло, не забудь поставить паузу при смерти yeбaнa и потапать на него, насмехайся над ними, но не становись посмешищем, выигрывай все игры, если команда сама не захотела или не заслужила поражения, выбор твой'
,           '7. all chat для тебя не существует, зачем тебе писать врагам что то, кроме "?" после убийств и ")" после падения трона?'
,           '8. убил мидера на фб? f9 + ?. у врага падает трон? ")" в all chat, но не больше, ты не clown.'
,           '9. гули нормальные, ты не токсик свинья и позер, ты нормальный, порофли с тимой если хочешь, хорошо общайся со своими ребятами если нужно, уважай тех, кто действительно этого достоин.'
,           '10. ЧСВ - положительное качество, ты сильнее и лучше всех, НО ты должен это оправдывать'
,           '11. будь верен своим идеалам. тебе не обязательно иметь гуля на аве, к чему это, поставь лил пипа или гослинга если хочешь, держись идеалов, но твой ник не должен быть отвратительным'
,           '12. никогда не пиши заглавными буквами. пиши размеренно и по правилам, не будь быдлом, ведь это низко. запомни в последний раз, ты не клоун, не позер и не нытик. ты - гуль, не позорься и не строй из себя не пойми что. соблюдай все правила, либо ты не гуль '
]
    try:
        i = int(i)
        return rules[i-1]
    except:
        return "\n".join(rules)

def generate():
    rifles = ["︻┳═一", "▄︻̷̿┻̿═━一"]
    symbols = "★彡༒☬☠︎♕乡☬牡マキグナルファ系路克瑞大阪市立学鎰命科ャマ能力ϒ人は妻スティ要通り玉宏¥サ丹谷Ѫ灯影伝鶐♠♡♢♣♤♥♦♧⁂☼☽☾✪✫✬✭✮✯"
    ranks = ["SSS", "SS+", "SS", "S+", "S", "A", "B", "C"]
    r = ["", "or feed", "or leave", "or afk", "or suicide", "или пудж с момкой", "или фид", "или лес", "or jungle"]
    rlist = ["dead inside", "dead outside", warpSymbols("дед внутри", 0, 2), "clown", warpSymbols("Touka", 0, 2),
             "мёртв внутри", "anti social", warpSymbols("sad", 0, 3), "sad", "killer", "чудище", "hate", "bury me",
             warpSymbols("bury me alive", 1, 3),
             '"i tired of this place"', warpSymbols("плевать на всех", 1, 3), "no brain",
             warpSymbols("feeling alive", 1, 3),
             warpSymbols("leave me on my own", 1, 3), "mode: ", "hide'n'seek",
             warpSymbols("dying as a lifestyle", 1, 3),
             warpSymbols("hate me as you do", 1, 2), warpSymbols("tilted", 0, 2), warpSymbols("ugly god", 0, 3),
             "i choose violence", "дед инсайд если че", "clownless", "broken", warpSymbols("kill me", 0, 3),
             "death",
             warpSymbols("death", 1, 3), "ghoul", warpSymbols("pain", 1, 3), warpSymbols("pain", 1, 3),
             symbols[random.randint(0, len(symbols) - 1)], str(random.randint(0, 9)) + " k pts",
             ranks[random.randint(0, len(ranks) - 1)] + " ранг",
             str(random.randint(0, 5)) + "-" + str(str(random.randint(0, 5))) + " pos " + r[
                 random.randint(0, len(r) - 1)],
             warpSymbols(rifles[random.randint(0, 1)], 0, 3),
             "zxc" * random.randint(1, 4), "пудж с момкой"]

    rlenght = random.randint(2, 4)
    n = ""
    for i in range(rlenght):
        n += rlist[random.randint(0, len(rlist) - 1)] + " "
    return n

if __name__ == '__main__':

    keyboard = {
        "one_time": False,
        "buttons": [
            [get_button('Сгенерировать', 'negative')],
            [get_button('Оскорбить', 'positive')],
            [get_button('Кодекс гуля', 'negative')]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
    keyboard = str(keyboard.decode("utf-8"))
    keyboard1 = {
        "one_time": False,
        "buttons": [
            [get_button('1', 'negative'), get_button('2', 'negative'),get_button('3', 'negative'),get_button('4', 'negative')],
            [get_button('5', 'negative'), get_button('6', 'negative'),get_button('7', 'negative'),get_button('8', 'negative')],
            [get_button('9', 'negative'), get_button('10', 'negative'),get_button('11', 'negative'),get_button('12', 'negative')],
            [get_button('Назад', 'positive'), get_button('Весь кодекс', 'negative')]
        ]
    }
    keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode("utf-8")
    keyboard1 = str(keyboard1.decode("utf-8"))

    #login = "+79633640554"
    #password = "fufodi56_iq1337"
    token = "c345715c3e4a527a0ed328fec87a303492352ea56b97e7da978cedfdbe33c24f3d982abf5e9e6aa351ec1"
    vk_session = vk_api.VkApi(token=token)
    # Работа с сообщениями
    longpoll = VkLongPoll(vk_session)
    # Основной цикл
    for event in longpoll.listen():
        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
            # Если оно имеет метку для бота
            if event.to_me:
                # Сообщение от пользователя
                request = event.text
                try:
                    request = int(request)
                    write_msg(event.user_id, generate_rule(request), keyboard=keyboard1)
                except:
                    if request == "Сгенерировать":
                        write_msg(event.user_id, generate(), keyboard=keyboard)
                    elif request == "Оскорбить":
                        write_msg(event.user_id, generate_damage(), keyboard=keyboard)
                    elif request == 'Кодекс гуля':
                        write_msg(event.user_id, 'гуль - не канеки кен на аве и не зитракс в подписках. гуль - это идеология, это культура. либо ты не называешь себя гулем, либо следуешь кодексу.', keyboard=keyboard1)
                    elif request == 'Назад':
                        write_msg(event.user_id, ')', keyboard=keyboard)
                    elif request == 'Весь кодекс':
                        write_msg(event.user_id, generate_rule('all'), keyboard=keyboard1)
                    else:
                    	write_msg(event.user_id, '?', keyboard=keyboard)

                print("New message from ", event.user_id)