import vk_api, json
import random
from vk_api.longpoll import VkLongPoll, VkEventType

def get_button(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \""+ "1" + "\"}",
            "label": str(text)
        },
        "color": str(color)
    }

keyboard=0
def write_msg(user_id, message, keyboard=keyboard):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0, "keyboard": keyboard})

def write_msg1(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0})

def warpSymbols(r, e, n):
    o = ""
    symbols = "★彡༒☬☠︎♕乡☬牡マキグナルファ系路克瑞大阪市立学鎰命科ャマ能力ϒ人は妻スティ要通り玉宏¥サ丹谷Ѫ灯影伝鶐♠♡♢♣♤♥♦♧⁂☼☽☾✪✫✬✭✮✯"
    for a in range(random.randint(e, n)):
        o += symbols[random.randint(0, len(symbols) - 1)]
    return o + r + o[::-1]

def generate_damage():
	list1 = ["бездарный", "тупоголовый", "ебанутый", "пизданутый", "безмозглый", "блядский", "отсталый", ""]
	list2 = ["сын шлюхи", "долбаёб", "бездарь", "хуесос", "выблядок", "кусок дерьма", "дегенерат", "уебан"]
	list3 = ["я тебе запрещаю разговаривать", "закрой ебало", "завали ебальник", "у тебя на аве", "у тебя мать шлюха", "с завода", 
	"без будущего", "я лучше тебя в каждом аспекте жизни", "никогда не заходи в эту игру"]
	resultlist = [list1, list2, list3]
	n = "" if random.randint(0, 1) else "ало "
	for i in range(3):
		n += resultlist[i][random.randint(0, len(resultlist[i])-1)] + " "
	return n

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
             symbols[random.randint(0, len(symbols) - 1)], str(random.randint(0, 9)) + "k pts",
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
            [get_button('Кодекс гулей', 'negative')]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
    keyboard = str(keyboard.decode("utf-8"))

    #login = "+7 963 364 05 54"
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
                if(request == "Сгенерировать"):
                	write_msg(event.user_id, generate())
                if(request == "Оскорбить"):
                	write_msg(event.user_id, generate_damage())
                print("New message from ", event.user_id)