from telebot import types
from telebot.types import Message

from database import DB
from utils.Question import Question
import telebot
import config
from utils import create_connection

message_text = "start"


def get_question(text: str, questions: list) -> Question | None:
    for question in questions:
        if text in question.questions:
            return question


connection = create_connection()
try:
    db = DB(connection)
    questions = db.get_questions()
finally:
    connection.close()
questions = [Question(question) for question in questions]

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)


@bot.message_handler()
def new_message(message: Message):
    question = get_question(message.text, questions)
    if question:
        markup = types.ReplyKeyboardMarkup()
        for button in question.answer.buttons:
            switch_button = types.KeyboardButton(text=button.button)
            markup.add(switch_button)
        message = bot.send_message(message.chat.id, question.answer.answer_text, reply_markup=markup)
        print(message)
    else:
        message = bot.send_message(message.chat.id, "Я тебя не понимаю")
        print(message)


bot.polling()


