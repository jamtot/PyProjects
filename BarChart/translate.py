"""Translate English text.

Can be translated to Spanish, Arabic, French or Portugese.
This uses the API for IBM Watson Language Translator.
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def translate():
    """Take in English text and translate.

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

    print()
    print("What language should I translate it to?")
    print("1) Spanish")
    print("2) Arabic")
    print("3) French")
    print("4) Portuguese")
    print()
    target = input("Select a language from the list above: ")

    if target == "1":
        target = 'es'
    elif target == "2":
        target = 'ar'
    elif target == "3":
        target = 'fr'
    elif target == "4":
        target = 'pt'

    translation = language_translator.translate(
        text=input("Please input text to be translated:\n"),
        model_id='en-'+target).get_result()

    return translation['translations'][0]['translation']

if __name__ == "__main__":
    print(translate())
