import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from environs import Env
from google_methods.detect_intent import detect_intent_texts
from logger import BotLogsHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('telegram_logging')


def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при выполнении команды /start."""
    user = update.effective_user
    update.message.reply_text(fr'Здравствуйте, {user.full_name}!')


def dialog_flow(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение пользователю от Dialogflow"""

    answer = detect_intent_texts(
        project_id=os.getenv('PROJECT_ID'),
        session_id=update.effective_user.id,
        msg=update.message.text,
        language_code='ru-RU'
    )[0]
    update.message.reply_text(answer)


def main() -> None:
    env = Env()
    env.read_env()

    updater = Updater(env('TOKEN_TG'))
    updater.logger.addHandler(BotLogsHandler(
        token=env('TOKEN_TG_LOG'),
        chat_id=env('CHAT_ID_LOG')
    ))
    dispatcher = updater.dispatcher
    updater.logger.warning('Бот Telegram запущен')
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, dialog_flow))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
