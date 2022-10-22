import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from environs import Env
from google.cloud import dialogflow

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def detect_intent_texts(project_id, session_id, msg, language_code):
    """Получение ответа от Dialogflow"""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))
    text_input = dialogflow.TextInput(text=msg, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text


def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при выполнении команды /start."""
    user = update.effective_user
    update.message.reply_text(fr'Здравствуйте, {user.full_name}!')


def echo(update: Update, context: CallbackContext) -> None:
    """Отправляет тоже сообщение пользователю"""
    answer = detect_intent_texts(
        project_id='elevated-oven-366303',
        session_id=update.effective_user.id,
        msg=update.message.text,
        language_code='ru-RU'
    )
    update.message.reply_text(answer)


def main() -> None:
    env = Env()
    env.read_env()
    updater = Updater(env('TOKEN'))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
