import vk_api as vk
import random
import logging

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.vk_api import VkApiMethod
from environs import Env

from google_methods.detect_intent import detect_intent_texts
from logger import BotLogsHandler
from time import sleep

logger = logging.getLogger('telegram_logging')


def dialog_flow(event, vk_api: VkApiMethod, env: Env) -> None:
    """Отправляет сообщение пользователю от Dialogflow"""

    answer, understand = detect_intent_texts(
        project_id=env('PROJECT_ID'),
        session_id=event.user_id,
        msg=event.text,
        language_code='ru-RU'
    )
    if understand:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )
    else:
        vk_api.messages.send(
            user_ids=env('ADMINS_VK'),
            message=f'Сообщение от пользователя https://vk.com/id{event.user_id}:\n"{event.text}"',
            random_id=random.randint(1, 1000)
        )


def main() -> None:
    env = Env()
    env.read_env()

    logger.addHandler(BotLogsHandler(
        token=env('TOKEN_TG_LOG'),
        chat_id=env('CHAT_ID_LOG')
    ))

    while True:

        try:
            vk_session = vk.VkApi(token=env('TOKEN_VK'))
            vk_api = vk_session.get_api()
            longpoll = VkLongPoll(vk_session)
            logger.warning('Бот ВК запущен')
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    dialog_flow(event, vk_api, env)

        except ConnectionError as err:
            logger.warning(f'Соединение было прервано: {err}', stack_info=True)
            sleep(5)
            continue
        except Exception as err:
            logger.exception(err)
            sleep(5)

    logger.critical('Бот ВК упал')


if __name__ == '__main__':
    main()
