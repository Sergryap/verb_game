# Бот для Telegram и VK на основе Dialogflow

Программа по реализации бота для условного онлайн-издательства, помогающего продвигать авторские блоги и публиковать книги.

Бот умеет отвечать на все типичные вопросы, а те что-то посложнее – перенаправляет на операторов.

По предварительной оценке, это на 70% сократит время ожидания ответа и на 90% повысит довольство жизнью сотрудников службы поддержки.

#### Пример результата для Telegram:

![demo_tg_bot](https://user-images.githubusercontent.com/99894266/197346997-9f2121c0-f1b1-4d48-b0c9-8e33fa84c8a1.gif)

#### Пример результата для ВКонтакте:

![demo_vk_bot](https://user-images.githubusercontent.com/99894266/197347013-d05f1e6c-f3c0-41f6-8da6-58387d7c25c1.gif)]

#### Примеры работающих ботов: *[Бот Telegram](https://t.me/sergryapbot)*, *[Бот Vk](https://vk.com/write-216628046)*

#### Что такое Dialogflow

Dialogflow — это платформа от Google для понимания естественного языка, которую можно использовать для создания омниканальных чат-ботов.

Если описать работу платформы несколькими фразами, то это выглядит примерно так. Dialogflow пытается распознать намерения пользователя на основе обучающих фраз, которые ему дают на этапе проектирования. Основываясь на этих обучающих фразах, Dialogflow понимает, какой ответ дать на тот или иной вопрос пользователя.
***
### Из чего состоит программа:

* В модуле ***bot_tg.py*** реализовано взаимодествие пользователя через интерфейс telegram
* В модуле ***bot_vk.py*** лизовано взаимодествие пользователя через сообщество Вконтакте
* В модуле ***loger.py*** реализован класс собственного обработчика логов
* В пакете ***google_methods*** реализованы методы взаимодействия с сервисом Dialogflow:

   ***detect_intent.py*** - получение ответного сообщения от сервиса Dialogflow на сообщение пользователя

   ***google_create_intents.py*** - загрузка обучающих фраз из [json-файла](https://github.com/Sergryap/verb_game/blob/master/google_methods/questions.json) с ответами и создание intents на их основе
   
### Необходимые переменные окружения и файлы:

Для работы программы необходимо создать файл `.env` в корне проекта содержащий переменные окружения:

* TOKEN_VK=<Ключ доступа для группы ботом Vk>
* TOKEN_TG=<Токен от основного бота Tg>
* TOKEN_TG_LOG=<Токен от бота Tg для отправки сообщений от логгера>
* CHAT_ID_LOG=<Id чата Tg для получения сообщений от логгера>
* ADMINS_VK=<Id администраторов Vk для общения с пользователями (через запятую без пробелов)>
* GOOGLE_APPLICATION_CREDENTIALS=<Путь до файла в формате json с ключами доступа к проекту в сервисе Google Cloud>
* PROJECT_ID=<Id проекта в Google Cloud>

В Google Cloud в разделе **IAM&Admin>Service accounts** для проекта необходимо получить файла в формате json с ключами доступа и разместить его по пути, указанному в GOOGLE_APPLICATION_CREDENTIALS.
<br>Файл должен иметь следующий вид:
```
{
  "type": "service_account",
  "project_id": "your app XXXXXX",
  "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "client_email": "xxxxxxxxxxxxxxx@xxxxxxxxxxxxxxxxxx.iam.gserviceaccount.com",
  "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxxxxxx.iam.gserviceaccount.com"
}
```










