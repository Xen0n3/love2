import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
# Создаём экземпляр бота
API_TOKEN = '7472500456:AAFYjScOyFaax5f5xaoGdDbewe0rPogTurM'
bot = telebot.TeleBot(API_TOKEN)


def get_crypto_price(crypto, currency="rub"):
    """Получает текущую цену криптовалюты."""
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto,  # Название криптовалюты (например, 'bitcoin', 'ethereum')
        "vs_currencies": currency  # Валюта (например, 'rub', 'usd')
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data[crypto][currency]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении курса: {e}")
        return None


# Словарь с городами и районами
cities = {
    
  "Москва": [
    "Центральный",
    "Северный",
    "Южный",
    "Западный",
    "Восточный",
    "Киевская",
    "Парк Культуры",
    "Савеловская",
    "Белорусская",
    "Таганская",
    "Тверская",
    "Юго-Западная",
    "Тропарёво",
    "Аэропорт",
    "Водный стадион",
    "Сокольники",
    "Щелковская",
    "Новокузнецкая",
    "Китай-город",
    "Площадь Революции"
  ],
  "Санкт-Петербург": [
    "Невский",
    "Адмиралтейский",
    "Василеостровский",
    "Лиговский проспект",
    "Московская",
    "Приморская",
    "Сенная площадь",
    "Проспект Ветеранов",
    "Чернышевская",
    "Купчино",
    "Звенигородская",
    "Парнас",
    "Политехническая",
    "Гражданский проспект",
    "Ладожская",
    "Выборгская",
    "Электросила",
    "Девяткино"
  ],
  "Новосибирск": [
    "Центральный",
    "Ленинский",
    "Октябрьский",
    "Дзержинский",
    "Советский",
    "Первомайский",
    "Калининский",
    "Заельцовский",
    "Кировский",
    "Новокузнецкая",
    "Площадь Ленина",
    "Речной вокзал",
    "Маршала Покрышкина",
    "Гагаринская",
    "Берёзовая роща"
  ],
  "Екатеринбург": [
    "Верх-Исетский",
    "Орджоникидзевский",
    "Кировский",
    "Железнодорожный",
    "Чкаловский",
    "Ленинский",
    "Уральская",
    "Ботаническая",
    "Площадь 1905 года",
    "Проспект Космонавтов",
    "Машиностроителей",
    "Уралмаш",
    "Чкаловская"
  ],
  "Казань": [
    "Вахитовский",
    "Советский",
    "Авиастроительный",
    "Приволжский",
    "Московский",
    "Кировский",
    "Ново-Савиновский",
    "Яшьлек",
    "Кремлёвская",
    "Площадь Тукая",
    "Аметьево",
    "Горки",
    "Северный вокзал",
    "Дубравная"
  ],
  "Нижний Новгород": [
    "Нижегородский",
    "Советский",
    "Сормовский",
    "Автозаводский",
    "Приокский",
    "Канавинский",
    "Ленинский",
    "Московский",
    "Гордеевская",
    "Чкаловская",
    "Стрелка",
    "Буревестник",
    "Московская",
    "Горьковская"
  ],
  "Челябинск": [
    "Центральный",
    "Калининский",
    "Тракторозаводский",
    "Ленинский",
    "Советский",
    "Металлургический",
    "Курчатовский",
    "Академический",
    "Меридиан",
    "Алое поле"
  ],
  "Самара": [
    "Самарский",
    "Октябрьский",
    "Ленинский",
    "Железнодорожный",
    "Промышленный",
    "Советский",
    "Куйбышевский",
    "Кировский",
    "Красноглинский",
    "Автозаводский",
    "Площадь Кирова",
    "Гагаринская",
    "Алабинская",
    "Безымянка"
  ],
  "Омск": [
    "Центральный",
    "Ленинский",
    "Октябрьский",
    "Советский",
    "Кировский",
    "Амурский",
    "Нефтяники",
    "Академический",
    "Зеленый остров",
    "Динамо"
  ],
  "Ростов-на-Дону": [
    "Железнодорожный",
    "Кировский",
    "Пролетарский",
    "Ворошиловский",
    "Первомайский",
    "Советский",
    "Ленинский",
    "Октябрьский",
    "Александровка",
    "Темерник"
  ],
  "Уфа": [
    "Калининский",
    "Дёмский",
    "Ленинский",
    "Кировский",
    "Советский",
    "Октябрьский",
    "Инорс",
    "Затон",
    "Сипайлово",
    "Центральный"
  ],
  "Красноярск": [
    "Центральный",
    "Ленинский",
    "Кировский",
    "Октябрьский",
    "Советский",
    "Свердловский",
    "Железнодорожный",
    "Взлётка",
    "Микрорайон Солнечный",
    "КрасТЭЦ"
  ],
  "Воронеж": [
    "Центральный",
    "Левобережный",
    "Железнодорожный",
    "Коминтерновский",
    "Советский",
    "Ленинский",
    "Северный",
    "Южный",
    "Берёзовая роща",
    "Площадь Ленина"
  ],
  "Пермь": [
    "Ленинский",
    "Свердловский",
    "Мотовилихинский",
    "Индустриальный",
    "Дзержинский",
    "Орджоникидзевский",
    "Бумажный",
    "Заводской",
    "Центральный",
    "Горнозаводский"
  ],
  "Волгоград": [
    "Краснооктябрьский",
    "Кировский",
    "Центральный",
    "Советский",
    "Тракторозаводский",
    "Красноармейский",
    "Дзержинский",
    "Ворошиловский",
    "Спартановка",
    "ВгТЗ"
  ],
  "Краснодар": [
    "Центральный",
    "Западный",
    "Карасунский",
    "Прикубанский",
    "Фестивальный",
    "Славянский",
    "Пашковский",
    "Юбилейный",
    "Гидрострой",
    "Микрорайон Восточный"
  ],
  "Тольятти": [
    "Автозаводский",
    "Центральный",
    "Комсомольский",
    "Портпоселок",
    "Жигулёвская долина",
    "Баныкин",
    "Фёдоровка",
    "Новая Волжская"
  ],
  "Ижевск": [
    "Октябрьский",
    "Индустриальный",
    "Устиновский",
    "Ленинский",
    "Советский"
  ],
    "Ульяновск": [
    "Засвияжский",
    "Ленинский",
    "Железнодорожный",
    "Заволжский",
    "Юго-Западный",
    "Центральный",
    "Новоульяновск",
    "Волга"
  ],
  "Барнаул": [
    "Центральный",
    "Индустриальный",
    "Железнодорожный",
    "Ленинский",
    "Октябрьский",
    "Пригородный",
    "Восточный",
    "Южный",
    "Западный"
  ]
}

# Списoк тoвaрoв
goods= ["Мeфeдpoн Kpиcтaллы VHQ | 0.5г | 1690 rub.",
"Мeфeдpoн Kpиcтaллы VHQ | 1г | 3190 rub.",
"Мeфeдpoн Kpиcтaллы VHQ | 2г | 6590 rub.",
"Мeфeдpoн мyкa | 1г | 2290 rub.",
"Мeфeдpoн мyкa | 2г | 3690 rub.",
"AльфaPVP Kpиcтaллы Зeлeнaя VHQ | 0.5г | 2490 rub.",
"AльфaPVP Kpиcтaллы Зeлeнaя VHQ | 1г | 4190 rub.",
"Aмфeтaмин | 1г | 3890 rub.",
"Aмфeтaмин | 2г | 5890 rub.",
"OПТ Мeфeдpoн Kpиcтaллы VHQ | 30г | 28990 rub.",
"OПТ Мeфeдpoн Kpиcтaллы VHQ | 100г | 92990 rub.",
"Экcтaзи ХТC 280mg | 1шт | 2590 rub.",
"Экcтaзи XTC - “Гpиб“ | 1шт | 1100 r.",
"VHQ KoKaин (Koлyмбия) White Rabbit | 1г | 11090 rub.",
"VHQ KoKaин (Koлyмбия) Пeчaть 40 | 0.5г | 5590 rub.",
"VHQ KoKaин (Koлyмбия) Пeчaть 40 | 1г | 9890 rub.",
"Бoшки “White Widow“ | 1г | 2899 rub.",
"Гaшиш “ICE-O-LATOR” | 1г | 3190 rub.",
"Бoшки ”Gorilla Kush” | 1г | 2869 rub."]

# Состояния пользователя
user_states = {}
admin_mode = {}

def get_cities_keyboard():
    #Создаёт Kлавиатуру с KнопKами городов в две Kолонки.
    keyboard = InlineKeyboardMarkup(row_width=2)
    city_buttons = [InlineKeyboardButton(text=city, callback_data=f"city_{city}") for city in cities.keys()]
    keyboard.add(*city_buttons)  # Передаём список кнопок как аргументы
    return keyboard

def get_districts_keyboard(city):
    #Создаёт клавиатуру с кнопками районов для выбранного города.
    keyboard = InlineKeyboardMarkup()
    for district in cities[city]:
        keyboard.add(InlineKeyboardButton(text=district, callback_data=f"district_{district}"))
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back_to_cities"))
    return keyboard

def get_goods_keyboard():
    #Создаёт клавиатуру с кнопками товаров.
    keyboard = InlineKeyboardMarkup()
    for good in goods:
        keyboard.add(InlineKeyboardButton(text=good, callback_data=f"g_{good}"))
    keyboard.add(InlineKeyboardButton(text="Назад", callback_data="back_to_districts"))
    return keyboard

def get_payment_keyboard():
    #Создаёт клавиатуру с кнопками выбора способа оплаты.
    keyboard = InlineKeyboardMarkup(row_width=2)
    usdt = InlineKeyboardButton(text="USDT TRC-20", callback_data="payment_usdt")
    btc = InlineKeyboardButton(text="BTC", callback_data="payment_btc")
    eth = InlineKeyboardButton(text="ETH ERC-20",callback_data="payment_eth")
    ton = InlineKeyboardButton(text="TON",callback_data="payment_ton")
    keyboard.add(btc,usdt,eth,ton)
    return keyboard


  
@bot.message_handler(commands=['start'])
def start_message(message):
    #Обрабатывает команду /start.
    chat_id = message.chat.id
    user_states[chat_id] = {"city": None, "district": None, "good_name": None, "good_weight": None, "good_price": None, "awaiting_hash": False}
    bot.send_message(chat_id, "*Выберите город:*", reply_markup=get_cities_keyboard(),parse_mode="MarkdownV2")

    
@bot.message_handler(commands=['chat'])
def start_chat(message):
    #Начинает чат с пользователем.
    try:
        args = message.text.split(maxsplit=1)
        target_user_id = int(args[1])  # ID пользователя
        admin_mode[message.chat.id] = target_user_id  # Связываем администратора с пользователем
        bot.send_message(message.chat.id, f"Чат с пользователем {target_user_id} активирован. Напишите сообщение для ответа.")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Используйте: /chat <ID пользователя>")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")
        
@bot.message_handler(commands=['send'])
def send_message_to_user(message):
    #Отправляет сообщение текущему пользователю.
    admin_chat_id = message.chat.id
    if admin_chat_id in admin_mode:
        try:
            # Извлекаем текст сообщения после команды /send
            target_user_id = admin_mode[admin_chat_id]
            text_to_send = message.text.split(maxsplit=1)[1]  # Текст после /send
            bot.send_message(target_user_id, text_to_send)  # Отправляем сообщение пользователю
            bot.send_message(admin_chat_id, "Сообщение отправлено.")
        except IndexError:
            bot.send_message(admin_chat_id, "Вы забыли указать текст после /send.")
        except Exception as e:
            bot.send_message(admin_chat_id, f"Ошибка при отправке сообщения: {str(e)}")
    else:
        bot.send_message(admin_chat_id, "У вас нет активного чата. Используйте /chat <ID пользователя>, чтобы начать.")    
        
@bot.message_handler(commands=['endchat'])
def end_chat(message):
      #Завершает текущую сессию чата с пользователем.
    admin_chat_id = message.chat.id  # ID администратора
    if admin_chat_id in admin_mode:
        del admin_mode[admin_chat_id]  # Удаляем текущую сессию
        bot.send_message(admin_chat_id, "Чат завершен.")
    else:
        bot.send_message(admin_chat_id, "У вас нет активных чатов.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("city_"))
def select_city(call):
    #Обрабатывает выбор города.
    chat_id = call.message.chat.id
    city = call.data.split("_")[1]
    user_states[chat_id]["city"] = city
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, f"*Выберите район:*", reply_markup=get_districts_keyboard(city),parse_mode="MarkdownV2")

@bot.callback_query_handler(func=lambda call: call.data.startswith("district_"))
def select_district(call):
    #Обрабатывает выбор района.
    chat_id = call.message.chat.id
    district = call.data.split("_")[1]
    user_states[chat_id]["district"] = district
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, f"*Выберите товар🛒:*", reply_markup=get_goods_keyboard(),parse_mode="MarkdownV2")


@bot.callback_query_handler(func=lambda call: call.data.startswith("g_"))
def select_good(call):
    #Обрабатывает выбор товара.
    chat_id = call.message.chat.id
    good_raw = call.data.split("_")[1]  # Получаем строку товара, например, "молоко | 1000г | 190 rub"

    # Разделяем строку на название, вес и цену
    parts = good_raw.split("|")
    if len(parts) == 3:  # Проверяем, что данные корректно разделены
        name = parts[0].strip()
        weight = parts[1].strip()
        price = parts[2].strip()

        # Сохраняем данные по отдельности в user_states
        user_states[chat_id]["good_name"] = name
        user_states[chat_id]["good_weight"] = weight
        user_states[chat_id]["good_price"] = price

        # Удаляем старое сообщение и отправляем новое с форматированными данными
        bot.delete_message(chat_id, call.message.message_id)
        bot.send_message(
            chat_id,
            f"*Товар:* {name}\n*Вес:* {weight}\n*Цена:* {price}\n*Город:* {user_states[chat_id]['city']}\n*Район:* {user_states[chat_id]['district']}\n\nВыберите способ оплаты:",
            reply_markup=get_payment_keyboard(),
            parse_mode="Markdown"
        )
    else:
        # Если формат товара неожиданно некорректный
        bot.send_message(chat_id, "Ошибка: неверный формат данных о товаре.")


@bot.callback_query_handler(func=lambda call: call.data.startswith("payment_"))
def process_payment(call):
    """Обрабатывает выбор способа оплаты."""
    chat_id = call.message.chat.id
    payment_method = call.data.split("_")[1]
    bot.delete_message(chat_id, call.message.message_id)

    # Определяем курс криптовалюты и рассчитываем сумму
    crypto_mapping = {
        "usdt": "tether",
        "btc": "bitcoin",
        "eth": "ethereum",
        "ton": "the-open-network"
    }
    selected_crypto = crypto_mapping.get(payment_method)
    if not selected_crypto:
        bot.send_message(chat_id, "Ошибка: выбран неверный метод оплаты.")
        return

    # Получаем цену товара в рублях
    price_rub = int(user_states[chat_id]["good_price"].split()[0])  # Цена товара (например, "190 rub")
    crypto_price = get_crypto_price(selected_crypto)
    
    if crypto_price is None:
        bot.send_message(chat_id, "Ошибка: не удалось получить курс криптовалюты. Попробуйте позже.")
        return

    # Рассчитываем сумму в криптовалюте
    amount_crypto = round(price_rub / crypto_price, 8)  # 8 знаков после запятой для точности

    # Формируем сообщение
    addresses = {
        "usdt": "TVtfZCt8oZhpV2mtySgd16RB2LfA7S543A",
        "btc": "1QBexgGucGHUkXW5Wye6rNHTpJpdabDRZF",
        "eth": "0x02fa27073e262114e3402831dd8a9b751e9f738a",
        "ton": "UQC-LURTcmYjph_ojRSfUU5DSWMzwFBRV3hhFSdOjSFywvvt"
    }
    address = addresses[payment_method]

    bot.send_message(
        chat_id,
        f"Оплатите сумму *{amount_crypto} {payment_method.upper()}*, номер счета:\n```\n{address}\n```\n\n❗*Внимательно проверьте сумму и сеть, в которой оплачиваете*❗\n\nПосле оплаты отправьте *хэш транзакции* в этот чат для проверки.\n\nДля перезапуска нажмите /start",
        parse_mode="Markdown"
    )

    # Устанавливаем режим ожидания хэша
    user_states[chat_id]["awaiting_hash"] = True


@bot.message_handler(func=lambda message: True)
def handle_transaction_hash(message):
    """Обрабатывает сообщения с хэшем транзакции."""
    chat_id = message.chat.id

    # Проверяем, ожидает ли бот хэш
    if not user_states.get(chat_id, {}).get("awaiting_hash", False):
        return

    text = message.text
    username = message.chat.username or "Без юзернейма"

    # Проверяем формат хэша
    if len(text) >= 40:  # Например, для BTC и ETH хэш — 64 символа
        admin_chat_id = 1309667346  # Ваш ID
        bot.send_message(
            admin_chat_id,
            f"Хэш: {text}\nЮзер: {username}\nID: {chat_id}\nИнформация о заказе: {user_states[chat_id]}",
        )
        bot.send_message(chat_id, "Хэш транзакции получен, проверка будет выполнена автоматически, ожидайте.")
        user_states[chat_id]["awaiting_hash"] = False  # Сбрасываем ожидание хэша
    else:
        bot.send_message(chat_id, "Пожалуйста, отправьте корректный хэш транзакции (обычно это строка из 64 символов).")


@bot.callback_query_handler(func=lambda call: call.data == "back_to_cities")
def back_to_cities(call):
    #Возврат к выбору города.
    chat_id = call.message.chat.id
    user_states[chat_id] = {"city": None, "district": None, "good": None}
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, "*Выберите город:*", reply_markup=get_cities_keyboard(),parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "back_to_districts")
def back_to_districts(call):
    #Возврат к выбору района.
    chat_id = call.message.chat.id
    city = user_states[chat_id]["city"]
    user_states[chat_id]["district"] = None
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, f"Вы выбрали город {city}. Теперь выберите район:", reply_markup=get_districts_keyboard(city))

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    #Пересылает сообщения от пользователей админу (мне) с их ID
    admin_chat_id = 1309667346
    user_id = message.chat.id
    username = message.chat.username or "Без юзернейма"
    text = message.text

    # Переслать сообщение админу
    bot.forward_message(admin_chat_id, user_id, message.message_id)

    # Дополнительно отправить информацию об ID
    bot.send_message(admin_chat_id, f"Сообщение от {user_id} ({username}): {text}")

    
# Запуск бота
bot.polling(none_stop=True)
