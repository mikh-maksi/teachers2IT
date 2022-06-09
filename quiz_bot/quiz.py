import logging

import pprint

# импорт API Telegramm
from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)

# импорт расширений библиотеки
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
)

poll_id = 0

# подключение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
def start(update, _):
    """Информация о том, что может сделать этот бот"""
    update.message.reply_text(
        'Введите `/poll` для участия в опросе, `/quiz` для участия в викторине или `/preview`'
        ' чтобы создать собственный опрос/викторину'
    )


def quiz(update, context):
    """Отправка заранее определенную викторину"""
    global poll_id
    # Вопрос викторины и ответы
    questions = 'Сколько яиц нужно для торта?'
    answer = ['1', '2', '4', '20']
    # посылаем сообщение с викториной, правильный ответ указывается
    # в `correct_option_id`, представляет собой индекс `answer`
    message = update.effective_message.reply_poll(
        questions, answer, type=Poll.QUIZ, correct_option_id=2
    )
    # print(message)
    print(message['poll']['id'])
    poll_id = message['poll']['id']
    
    # Сохраним промежуточные данные викторины в `bot_data` для использования в `receive_quiz_answer`
    payload = { # ключом словаря с данными будет `id` викторины
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    # print(payload)
    context.bot_data.update(payload)
    print(context.bot_data)

def receive_quiz_answer(update, context):
    """Закрываем викторину после того, как ее прошли три участника"""
    # бот может получать обновления уже закрытого опроса, которые уже не волнуют
    print(update.poll.total_voter_count)
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 3:
        try:
            quiz_data = context.bot_data[update.poll.id]
        except KeyError: # Это означает, что это ответ из старой викторины
            return
        context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])
        print("stop")



if __name__ == '__main__':
    updater = Updater("")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('quiz', quiz))

    updater.start_polling()
    updater.idle()
