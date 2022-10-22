from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, msg, language_code):
    """Получение ответа от Dialogflow"""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    text_input = dialogflow.TextInput(text=msg, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={'session': session, 'query_input': query_input})
    understand = not response.query_result.intent.is_fallback

    return response.query_result.fulfillment_text, understand
