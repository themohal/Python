#First we import LanguageTranslatorV3 from ibm_watson and authenticatior to make connection
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#The service endpoint is based on the location of the service instance,
#  we store the information in the variable URL.
#  To find out which URL to use, view the service credentials.
url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/62f96f07-4b42-4ecd-bafc-5e316f106af0'
#You require an API key, and you can obtain the key
apikey_lt='W3LM4Mkuh7QQQ9bxJPOQhjJ14ePM7wc5uFUI8cISyC1e'
#API requests require a version parameter that takes a date 
# in the format version=YYYY-MM-DD. 
# This lab describes the current version of Language Translator, 2018-05-01
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
#we create a Language Translator object language_translator:
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)
#We can get a Lists the languages that the service can identify.
#  The method Returns the language code. 
# For example English (en) to Spanis (es) and name of each language.
from pandas.io.json import json_normalize

print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))
#We can use the method translate this will translate the text. 
# The parameter text is the text. 
# Model_id is the type of model we would like to use use we use list the the langwich .
#  In this case, we set it to 'en-es' or English to Spanish. 
# We get a Detailed Response object translation_response
recognized_text="Hello World! I am Farjad and AI Expert."

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
print(translation_response)
#The result is a dictionary.
translation=translation_response.get_result()
print(translation)
#We can obtain the actual translation as a string as follows:
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)
#We can translate back to English 
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
#We can obtain the actual translation as a string as follows:
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)
#We can convert it to french as well:
French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()
print(French_translation['translations'][0]['translation'])