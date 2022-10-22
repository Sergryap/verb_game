import vk_api as vk
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env
from bot_telegram import detect_intent_texts


def dialog_flow(event, vk_api, env):

    answer = detect_intent_texts(
        project_id=env('PROJECT_ID'),
        session_id=event.user_id,
        msg=event.text,
        language_code='ru-RU'
    )
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1, 1000)
    )


def main():
    env = Env()
    env.read_env()

    vk_session = vk.VkApi(token=env('TOKEN_VK'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog_flow(event, vk_api, env)


if __name__ == '__main__':
    main()
