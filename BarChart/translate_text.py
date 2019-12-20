"""Translate English text.

Can be translated to Spanish, Arabic, French or Portugese.
This uses the API for IBM Watson Language Translator.
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def translate(text_to_translate, language="es"):
    """Translate text passed in.

    The API key and URL are read in from external
    files to prevent someone using my unique key.
    """
    path = '/home/jamtot/IBM/'

    api_key = ''
    with open(path + 'API_KEY.txt', 'r') as api_file:
        api_key = api_file.read().rstrip('\n')

    url = ''
    with open(path + 'URL.txt', 'r') as url_file:
        url = url_file.read().rstrip('\n')

    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    translation = language_translator.translate(
        text=text_to_translate,
        model_id='en-'+language).get_result()

    return translation['translations'][0]['translation']

if __name__ == "__main__":
    print(translate())
