# Бот для Telegram и VK на основе Dialogflow

Программа по реализации бота для условного онлайн-издательства, помогающего продвигать авторские блоги и публиковать книги.

Бот умеет отвечать на все типичные вопросы, а те что-то посложнее – перенаправляет на операторов.

По предварительной оценке, это на 70% сократит время ожидания ответа и на 90% повысит довольство жизнью сотрудников службы поддержки.

#### Пример результата для Telegram:

![demo_tg_bot](https://user-images.githubusercontent.com/99894266/197346997-9f2121c0-f1b1-4d48-b0c9-8e33fa84c8a1.gif)

#### Пример результата для ВКонтакте:

![demo_vk_bot](https://user-images.githubusercontent.com/99894266/197347013-d05f1e6c-f3c0-41f6-8da6-58387d7c25c1.gif)]

##### Примеры работающих ботов: *[Бот Telegram](https://t.me/sergryapbot)*, *[Бот Vk](https://vk.com/write-216628046)*
<br>

### Что такое Dialogflow

[Dialogflow](https://dialogflow.cloud.google.com) — это платформа от Google для понимания естественного языка, которую можно использовать для создания омниканальных чат-ботов.

Если описать работу платформы несколькими фразами, то это выглядит примерно так. Dialogflow пытается распознать намерения пользователя на основе обучающих фраз, которые ему дают на этапе проектирования. Основываясь на этих обучающих фразах, Dialogflow понимает, какой ответ дать на тот или иной вопрос пользователя.
***
### Из чего состоит программа:

* В модуле ***bot_tg.py*** реализовано взаимодествие пользователя через интерфейс telegram
* В модуле ***bot_vk.py*** реализовано взаимодествие пользователя через сообщество Вконтакте
* В модуле ***logger.py*** реализован класс собственного обработчика логов
* В пакете ***google_methods*** реализованы методы взаимодействия с сервисом Dialogflow:

   ***detect_intent.py*** - получение ответного сообщения от сервиса Dialogflow на сообщение пользователя

   ***create_intents.py*** - загрузка обучающих фраз из [json-файла](https://github.com/Sergryap/verb_game/blob/master/google_methods/questions.json) с ответами и создание intents на их основе
   
### Необходимые переменные окружения и файлы:

Для работы программы необходимо создать файл `.env` в корне проекта, содержащий переменные окружения:
```
TOKEN_VK=<Ключ доступа для группы с ботом Vk>
TOKEN_TG=<Токен от основного бота Tg>
TOKEN_TG_LOG=<Токен от бота Tg для отправки сообщений от логгера>
CHAT_ID_LOG=<Id чата Tg для получения сообщений от логгера>
ADMINS_VK=<Id администраторов Vk для общения с пользователями (через запятую без пробелов)>
GOOGLE_APPLICATION_CREDENTIALS=<Путь до файла в формате json с ключами доступа к проекту в сервисе Google Cloud>
PROJECT_ID=<Id проекта в Google Cloud>
```

В Google Cloud в разделе **[IAM&Admin>Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)** для проекта необходимо получить файл в формате json с ключами доступа и разместить его по пути, указанному в GOOGLE_APPLICATION_CREDENTIALS.
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
Файлы `.profile` и `Procfile` необходимы для деплоя на сервие [Heroku](https://heroku.com)
***
## Пример установки
#### Загрузите репозиторий проекта:
`git clone https://github.com/Sergryap/verb_game.git`
#### Создайте и активируйте виртуальное окружение в корневой папке проекта:
```
cd verb_game/
python3 -m venv venv
source venv/bin/activate
```
#### Установите необходимые зависимости:
`pip install -r requirements.txt`

![Screenshot from 2022-10-24 18-58-41](https://user-images.githubusercontent.com/99894266/197549304-f233ad0a-7d59-4047-94b9-4106f775d5be.png)
#### Создайте в корне проекта файл `.env` и запишите в него необходимые ключи:
`nano .env`

#### Разместите файл json с ключами доступа в корне проекта:

![Screenshot from 2022-10-24 19-06-28](https://user-images.githubusercontent.com/99894266/197549928-3257a86c-b917-4902-a129-b437c19c6501.png)

#### Чтобы запустить тренировку бота выполните команду:
`python3 google_methods/create_intents.py`

Этой командой создадутся Intents в сервие DialogFlow на основании данных файла `/google_methods/questions.json`

#### Запустите бота для tg и vk:
`python3 bot_tg.py | python3 bot_vk.py`

![Screenshot from 2022-10-24 19-55-21](https://user-images.githubusercontent.com/99894266/197557684-d10825b1-2be8-4768-8202-cffa774347c0.png)

#### После запуска ботов вам придут сообщения от логгера в Tg:

![Screenshot from 2022-10-24 19-08-07](https://user-images.githubusercontent.com/99894266/197558118-61fbdbca-c2df-4e5e-a820-8552f5236608.png)


























