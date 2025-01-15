import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("7522791191:AAHVuXv2h2LfxTK0oVy7fEQjwFiLYsaUQOk")
password = "admin777"  # Установи пароль
user_access = {}  # Список пользователей с доступом

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Привет! Чтобы открыть приложение, введите пароль:"
    )

@bot.message_handler(func=lambda message: True)
def check_password(message):
    if message.text == password:
        user_access[message.chat.id] = True
        bot.send_message(message.chat.id, "Пароль верный! Теперь у вас есть доступ к приложению.")
        send_button(message.chat.id)  # Показываем кнопку только после ввода пароля
    else:
        bot.send_message(message.chat.id, "Неверный пароль. Попробуйте снова.")

def send_button(chat_id):
    markup = InlineKeyboardMarkup()
    # Кнопка с ссылкой на приложение
    btn = InlineKeyboardButton("Open Mod 🎰", url="https://t.me/skript1win_bot/skriptbot")
    markup.add(btn)
    bot.send_message(chat_id, "Теперь можно открыть модуль:", reply_markup=markup)

bot.polling()
