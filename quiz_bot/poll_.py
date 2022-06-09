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

# poll_id = 0

# подключение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
def strt():
    f = open('poll_data.csv','w')
    f.close()



def fl(username,firstname,lastname,fid,answer):
    f = open('poll_data.csv','a')
    file_out = f"{username};{firstname};{lastname};{fid};{answer};"
    print("CSV")
    print(file_out)
    f.write(file_out+'\n')
    f.close()


def file_(update, _):
    strt():


def start(update, _):
    """Информация о том, что может сделать этот бот"""
    update.message.reply_text(
        'Введите `/poll` для участия в опросе'
    )

def poll(update, context):
    # Вопрос опроса и его ответы.
    questions = "Как дела?"
    answer = ["Нормально", "Хорошо", "Отлично", "Супер!"]
    # Отправляем опрос в чат
    message = context.bot.send_poll(
        update.effective_chat.id, questions, answer,
        is_anonymous=False, allows_multiple_answers=True,
    )
    # Сохраним информацию опроса в `bot_data` для последующего
    # использования в функции `receive_poll_answer`
    payload = { # ключом словаря с данными будет `id` опроса
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    # сохранение промежуточных результатов в `bot_data`
    context.bot_data.update(payload)


def receive_poll_answer(update, context):
    """Итоги опроса пользователей"""
    print('recive')
    # global poll_id
    # print(poll_id)
    answer = update.poll_answer
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"]
        print(questions)
    except KeyError:  # Это ответ на старый опрос
        return
    selected_options = answer.option_ids
    print(update.effective_user)
    out_string = str(update.effective_user['id']) + ' '+str(selected_options[0])
    fl(str(update.effective_user['username']),str(update.effective_user['first_name']),str(update.effective_user['last_name']),str(update.effective_user['id']),str(selected_options[0]))
    print(out_string)
    answer_string = ""
    # подсчет и оформление результатов
    for question_id in selected_options:
        if question_id != selected_options[-1]:
            answer_string += questions[question_id] + " и "
            print (answer_string)
        else:
            answer_string += questions[question_id]

    context.bot.send_message(
        context.bot_data[poll_id]["chat_id"],
        f"{update.effective_user.mention_html()} => {answer_string}!",
        parse_mode=ParseMode.HTML,
    )
    # изменение промежуточных результатов в `bot_data`
    print(poll_id)
    print(context.bot_data[poll_id])
    context.bot_data[poll_id]["answers"] += 1
    print(context.bot_data[poll_id]["answers"])
    # Закрываем опрос после того, как проголосовали три участника
    if context.bot_data[poll_id]["answers"] == 2:
        context.bot.stop_poll(
            context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
        )


if __name__ == '__main__':
    updater = Updater("")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))    
    dispatcher.add_handler(CommandHandler('file_', start))

    dispatcher.add_handler(CommandHandler('poll', poll))
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    dispatcher.add_handler(CommandHandler('recive', receive_poll_answer))
    updater.start_polling()
    updater.idle()