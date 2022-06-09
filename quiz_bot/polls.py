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


q_arr = ["Как дела?","Как погода?"]

ans_arr = [["Нормально", "Хорошо", "Отлично", "Супер!"],
        ["Нормально", "Хорошо", "Отлично", "Супер!"]]

# poll_id = 0

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

def poll(update, context):
    """Отправка заранее подготовленного опроса"""
    # Вопрос опроса и его ответы.
    questions = "Как дела?"
    answer = ["Нормально", "Хорошо", "Отлично", "Супер!"]
    # Отправляем опрос в чат
    message = context.bot.send_poll(
        update.effective_chat.id, questions, answer,
        is_anonymous=False, allows_multiple_answers=True,
    )
    print(answer)
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
    out_string = str(update.effective_user['id']) + ' '+str(selected_options[0])
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
    context.bot_data[poll_id]["answers"] += 1
    # Закрываем опрос после того, как проголосовали три участника
    # if context.bot_data[poll_id]["answers"] == 3:
    #     context.bot.stop_poll(
    #         context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
    #     )


if __name__ == '__main__':
    updater = Updater("5101987677:AAHm9vcl71p0-h_ZdIX6Clcfb3hbcdhTec8")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('quiz', quiz))
    dispatcher.add_handler(CommandHandler('poll', poll))
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    dispatcher.add_handler(CommandHandler('recive', receive_poll_answer))
    dispatcher.add_handler(PollHandler(receive_quiz_answer))
    updater.start_polling()
    updater.idle()