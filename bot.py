import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from environs import Env

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при выполнении команды /start."""
    user = update.effective_user
    update.message.reply_text(fr'Здравствуйте, {user.full_name}!')


def echo(update: Update, context: CallbackContext) -> None:
    """Отправляет тоже сообщение пользователю"""
    update.message.reply_text(update.message.text)


def main() -> None:
    env = Env()
    env.read_env()
    updater = Updater(env("TOKEN"))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
