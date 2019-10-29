import json
import os

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

WATSON_SECRET = os.getenv('WATSON_SECRET')
if WATSON_SECRET is not None:
    authenticator = IAMAuthenticator(WATSON_SECRET)
    lang_processor = NaturalLanguageUnderstandingV1(version='2019-07-12', authenticator=authenticator)
    lang_processor.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')


def analyze(text):
    if WATSON_SECRET is None:
        return {}

    print('Beginning Analysis of the Text: ' + text)
    result = lang_processor.analyze(
        text=text,
        features=Features(
            entities=EntitiesOptions(
                emotion=True,
                sentiment=True,
                limit=2
            ),
            emotion=EmotionOptions()
        )
    ).get_result()

    json_dump = json.dumps(result, indent=2)
    json_load = json.loads(json_dump)

    emotions = json_load['emotion']['document']['emotion']

    return emotions


# Uncomment the below lines to test the analyzer output
# Approximate Expectation: { max_key: joy, max_val: 0.609666 }
# test_string = "Abraham Lincoln was this countries best president."
# test_result = analyze(test_string)
# print(test_result)
