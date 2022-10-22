import json

from google.cloud import dialogflow
from environs import Env
from typing import Union


def create_intent(
        project_id: str,
        display_name: str,
        training_phrases_parts: Union[list, tuple],
        message_texts: Union[list, tuple]
) -> None:
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={'parent': parent, 'intent': intent}
    )

    print('Intent created: {}'.format(response))


def create_intents(file_phrases: str, project_id: str) -> None:
    """Создание intents на основе списка фраз и ответов из файла"""
    with open(file_phrases, 'r') as f:
        file = f.read()
    phrases = json.loads(file)

    for display_name, questions in phrases.items():
        create_intent(
            project_id=project_id,
            display_name=display_name,
            training_phrases_parts=questions['questions'],
            message_texts=(questions['answer'], )
        )


def main() -> None:
    env = Env()
    env.read_env()
    create_intents('google_methods/questions.json', env('PROJECT_ID'))


if __name__ == '__main__':
    main()
