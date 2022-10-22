import logging
from telegram.bot import Bot


class BotLogsHandler(logging.Handler):

    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord) -> None:
        log_entry = self.format(record)
        send_message(token=self.token, chat_id=self.chat_id, msg=log_entry)


def send_message(token, chat_id, msg):
    bot = Bot(token)
    bot.send_message(chat_id, msg)
