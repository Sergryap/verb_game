from typing import Tuple
from google.cloud import dialogflow


def detect_intent_texts(project_id: str, session_id: str, msg: str, language_code: str) -> Tuple[str, bool]:
    """Получение ответа от Dialogflow"""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    text_input = dialogflow.TextInput(text=msg, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={'session': session, 'query_input': query_input})
    message_to_send = response.query_result.fulfillment_text
    understand = not response.query_result.intent.is_fallback

    return message_to_send, understand
